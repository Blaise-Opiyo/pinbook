from django.shortcuts import render,redirect
from .models import ProfileData
from django.contrib.auth.models import User
from .forms import CreateProfileData,CreatePin,CreateComment
from .models import Follow,Pin,Comment,PinLikes,PinDislikes
from django.contrib.auth.decorators import login_required

# Create your views here.
#PINS LIST
@login_required(login_url="accounts:login")
def pins_list(request):
    profileData = ProfileData.objects.all()
    loggedInUser = User.objects.get(username = request.user.username)

    profileExists = ProfileData.objects.all().filter(username = request.user).count()

    pinform = CreatePin()
    postedpin = Pin.objects.all()

    commentForm = CreateComment()
    pinComment = Comment.objects.all()

    postedPinComments = {}
    for pin in postedpin:
        comments = Comment.objects.all().filter(pinid = pin.id).count()
        postedPinComments[pin.id] = comments   

    pinLikes = {}
    has_liked = {}
    for pin in postedpin:
        #Count the number of likes for a particular pin
        likes = PinLikes.objects.all().filter(pin = pin.id).count()
        pinLikes[pin.id] = likes
        #Check whether the logged in user has liked a particular pin
        like_pin = PinLikes.objects.all().filter(author = request.user,pin = pin.id).count()
        has_liked[pin.id] = like_pin

    pinDislikes = {}
    has_disliked = {}
    for pin in postedpin:
        #Count the number of dislikes for a particular pin
        dislikes = PinDislikes.objects.all().filter(pin = pin.id).count()
        pinDislikes[pin.id] = dislikes
        #check whether the logged in user has disliked a particlar pin
        dislike_pin = PinDislikes.objects.all().filter(author = request.user,pin = pin.id).count()
        has_disliked[pin.id] = dislike_pin

    return render(request,'pins/pins_list.html',{'profileData':profileData,'loggedInUser':loggedInUser,
    'profileExists':profileExists,'pinform':pinform,'postedpin':postedpin,'commentForm':commentForm,
    'pinComment':pinComment,'postedPinComments':postedPinComments,'pinLikes':pinLikes,'pinDislikes':pinDislikes,
    'has_liked':has_liked,'has_disliked':has_disliked})

def pin_post(request):
    if request.method == 'POST':
        pin = CreatePin(request.POST)
        if pin.is_valid():
            new_pin = pin.save(commit=False)
            new_pin.author = request.user
            new_pin.save()
            return redirect('pins:list')

def pin_comment(request):
    if request.method == 'POST':
        comment = CreateComment(request.POST)
        if comment.is_valid():
            new_comment = comment.save(commit=False)
            new_comment.author = request.user
            new_comment.pinid = request.POST.get('pinid')
            new_comment.save()
            return redirect('pins:list')


def pin_like(request):
    if request.method == 'POST':
        like_exists = PinLikes.objects.filter(pin=request.POST.get('pinid'),author=request.user)
        dislike_exists = PinDislikes.objects.filter(pin=request.POST.get('pinid'),author=request.user)
        if like_exists.count() > 0:
            like_exists.delete()
            if dislike_exists.count() > 0:
                dislike_exists.delete()
        else:
            if dislike_exists.count() > 0:
                dislike_exists.delete()

            like1 = PinLikes()
            like1.author = request.user
            like1.pin = request.POST.get('pinid')
            like1.like = request.POST.get('like')
            like1.save()
            
    return redirect('pins:list')

def pin_dislike(request):
    if request.method == 'POST':
        dislike_exists = PinDislikes.objects.filter(pin=request.POST.get('pinid'),author=request.user)
        like_exists = PinLikes.objects.filter(pin=request.POST.get('pinid'),author=request.user)

        if dislike_exists.count() > 0:
            dislike_exists.delete()
            if like_exists.count() > 0:
                like_exists.delete()
        else:
            if like_exists.count() > 0:
                like_exists.delete()

            dislike1 = PinDislikes()
            dislike1.author = request.user
            dislike1.pin = request.POST.get('pinid')
            dislike1.dislike = request.POST.get('dislike')
            dislike1.save()
    return redirect('pins:list')



#PINS PROFILE
@login_required(login_url="accounts:login")
def pins_profile(request):
    profileData = ProfileData.objects.all()
    
    profileExists = ProfileData.objects.all().filter(username = request.user).count()
    
    LoggedInUser = User.objects.get(username=request.user.username)
    users = User.objects.all()

    pinPosts = Pin.objects.all().filter(author = request.user).count()

    followRecord = Follow.objects.all()
    followers = Follow.objects.all().filter(followed = request.user).count()
    following = Follow.objects.all().filter(follower = request.user).count()
    
    if request.method == 'POST':
        createProfileDataForm = CreateProfileData(request.POST,request.FILES)
        if createProfileDataForm.is_valid():
            profileDataExists = ProfileData.objects.all().filter(username = request.user)
            if profileDataExists.count() > 0:
                profileDataExists.delete()
                createDataFormInstance = createProfileDataForm.save(commit=False)
                user_name = request.user.username
                new_username = user_name.replace(" ","-")
                slug = new_username.upper()
                createDataFormInstance.slug = slug
                createDataFormInstance.username = request.user
                createDataFormInstance.save()
                return redirect('pins:profile')
            else:
                createDataFormInstance = createProfileDataForm.save(commit=False)
                user_name = request.user.username
                new_username = user_name.replace(" ","-")
                slug = new_username.lower()
                createDataFormInstance.slug = slug
                createDataFormInstance.username = request.user
                createDataFormInstance.save()
                return redirect('pins:profile')
    else:
        createProfileDataForm = CreateProfileData()
    
    return render(request,'pins/pins_profile.html',{'LoggedInUser':LoggedInUser,'profileData':profileData,
    'createProfileDataForm':createProfileDataForm,'pinPosts':pinPosts,'followRecord':followRecord,'followers':followers,
    'following':following,'profileExists':profileExists,'users':users})

def pins_follow(request):
    if request.method == 'POST':
        followExists = Follow.objects.all().filter(followed=request.POST.get('followed'),follower=request.user)
        if followExists.count() > 0:
            followExists.delete()
            newFollow = Follow()
            newFollow.follower = request.user
            newFollow.followed = request.POST.get('followed')
            newFollow.following = request.POST.get('following')
            newFollow.save()
        else:
            newFollow = Follow()
            newFollow.follower = request.user
            newFollow.followed = request.POST.get('followed')
            newFollow.following = request.POST.get('following')
            newFollow.save()
    
    return redirect('pins:profile')

def profile_following(request,slug):
    profile = ProfileData.objects.get(slug=slug)

    pinPosts = Pin.objects.all().filter(author = profile.username).count()

    followInfo = Follow.objects.all()
    followers = followInfo.filter(followed=profile.username).count()
    following = followInfo.filter(follower=profile.username).count()
    return render(request,'pins/profile_following.html',{'profile':profile,'pinPosts':pinPosts,'followInfo':followInfo,
    'followers':followers,'following':following})