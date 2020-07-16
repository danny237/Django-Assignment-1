from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('',views.home, name='home'),
    path('blogs', views.blog_list, name='blog_list'),
    path('post_detail/<int:post_id>', views.post_detail, name='detail')
]