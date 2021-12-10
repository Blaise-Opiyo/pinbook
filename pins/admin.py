from django.contrib import admin
from .models import ProfileData,Follow,Pin,Comment,PinLikes,PinDislikes


# Register your models here.
admin.site.register(ProfileData)
admin.site.register(Follow)
admin.site.register(Pin)
admin.site.register(Comment)
admin.site.register(PinLikes)
admin.site.register(PinDislikes)