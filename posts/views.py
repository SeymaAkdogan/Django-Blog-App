from django.shortcuts import render

from posts.models import Category, Post


def index(request):
    last_ten = Post.objects.filter(is_published=True,deleted_at=None,status='published')[:5]
    posts = reversed(last_ten)

    return render(request,'post/home.html',{
        'posts' : posts,
        'categories' : Category.objects.all()
    })

def getAllPost(request):
    posts = Post.objects.filter(deleted_at=None,status='published',is_published=True)
    return render(request,'post/list.html',{
        'posts' : posts,
        'featured_posts' : Post.objects.filter(status='draft',deleted_at=None,is_published=True),
        'categories' : Category.objects.all()
    })

def post_details(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request,'post/post_detail.html',{
        'post' : post
    })

def posts_by_categories(request,slug):
    return render(request,'post/list.html',{
        'posts' : Category.objects.get(category_slug=slug).post_set.filter(is_published=True,deleted_at=None,status='published'),
        'featured_posts' : Post.objects.filter(status='draft',deleted_at=None,is_published=True),
        'categories' : Category.objects.all()
    })