from django.urls import path
from .views import login, logout, signup, update_profile, profile


app_name = 'users' 

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('update-profile/', update_profile, name='update-profile'),
    path('profile/', profile, name='profile')
    
]