from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('login/', views.users_login, name='login'),
    path('signup/', views.users_signup, name='signup'),
    path('logout/', views.users_logout, name='logout'),

]