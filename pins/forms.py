from django import forms
from .models import ProfileData,Pin,Comment

class CreateProfileData(forms.ModelForm):
    class Meta:
        model = ProfileData
        fields = ['bio','location','profilePic']

    def __init__(self, *args, **kwargs):
        super(CreateProfileData, self).__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs['class'] = 'update-profile-details-bio'
        self.fields['location'].widget.attrs['class'] = 'update-profile-details-location'

        self.fields['bio'].widget.attrs['placeholder'] = 'bio'
        self.fields['location'].widget.attrs['placeholder'] = 'location'

class CreatePin(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CreatePin, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['class'] = 'make-a-post-postinput'

        self.fields['content'].widget.attrs['placeholder'] = 'post a pin'


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CreateComment, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['class'] = 'comment-input'

        self.fields['content'].widget.attrs['placeholder'] = 'comment on pin'