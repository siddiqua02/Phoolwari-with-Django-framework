from django.urls import path
from user.views import signup,signin,signout,add_address
urlpatterns = [
    path('sign up/',signup,name='signup'),
    path('sign in/',signin,name='signin'),
    path('sign out/',signout,name='signout'),
    path('add_address/',add_address,name='add_address')
    
]
