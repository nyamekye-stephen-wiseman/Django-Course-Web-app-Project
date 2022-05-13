from django.urls import path
from .views import profiles, userProfile, loginUser, logoutUser, registerUser



urlpatterns = [
    path('', profiles, name="profiles"),
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('user-profile/<str:pk>/', userProfile, name="user-profile"),
    path('register/', registerUser, name="register"),
    
]