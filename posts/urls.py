from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='home'),
    path("posts",views.getAllPost,name='getAllPost'),
    path("post/<slug:slug>",views.post_details,name='post_details'),
    path("categories/<slug:slug>",views.posts_by_categories,name='posts_by_categories')
]