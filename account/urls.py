from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.users_login),
    path('signup/', views.users_signup),
    path('logout/', views.users_logout),

]