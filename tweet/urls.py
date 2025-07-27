from . import views
from django.urls import path

urlpatterns = [
    path('tweetlist/',views.tweetlist,name='tweetlist'),
    path('create/',views.tweetcreate ,name='tweetcreate'),
    path('<int:tweetid/edit/',views.tweetedit ,name='tweetedit'),
    path('<int:tweetid/delete/',views.tweetdelete ,name='tweetdelete'),
    path('register/',views.register,name='register'),
    
    
]
