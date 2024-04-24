from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('<str:title>', views.post_detail, name='post'),
]
