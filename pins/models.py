from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileData(models.Model):
    username = models.ForeignKey(User,db_column='username', on_delete=models.CASCADE,default=None)
    bio = models.CharField(max_length = 250)
    location = models.CharField(max_length = 20)
    date = models.DateTimeField(auto_now_add = True)
    profilePic = models.ImageField(default='/default_profile_pic.png',blank=True)
    slug = models.SlugField(default="invalid-url")

    def __str__(self):
        return str(self.username)

class Follow(models.Model):
    follower = models.CharField(max_length = 20)
    followed = models.CharField(max_length = 20)
    following = models.IntegerField()

    def __str__(self):
        return self.followed

class Pin(models.Model):
    author = models.ForeignKey(User, db_column='username',on_delete=models.CASCADE,default=None)
    content = models.CharField(max_length = 250)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.content[:40] + "..."

class Comment(models.Model):
    pinid = models.IntegerField()
    author = models.ForeignKey(User, db_column='username',on_delete=models.CASCADE,default=None)
    content = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.content[:30] + "..."

class PinLikes(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    pin = models.IntegerField()
    like = models.IntegerField()

    def __str__ (self):
        return str(self.pin)

class PinDislikes(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    pin = models.IntegerField()
    dislike = models.IntegerField()

    def __str__(self):
        return str(self.pin)
