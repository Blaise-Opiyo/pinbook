from django.urls import path
from .import views

app_name = 'pins'

urlpatterns = [
    #pins list
    path('',views.pins_list,name='list'),
    path('post/',views.pin_post,name='post'),
    path('comment/',views.pin_comment,name='comment'),
    path('like/',views.pin_like,name="like"),
    path('dislike/',views.pin_dislike,name="dislike"),

    #pins profile
    path('profile/',views.pins_profile,name='profile'),
    path('follow/',views.pins_follow,name='follow'),
    path('<str:slug>/',views.profile_following,name='profile_following')
]
