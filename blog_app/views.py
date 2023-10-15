from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . models import Blog,Category
from django.db.models import Q

# Create your views here.

def posts_by_category(request,category_id):
    posts = Blog.objects.filter(category=category_id,status='Published')
    category = get_object_or_404(Category,id=category_id)
    context ={
        'posts':posts,
        'category':category
    }
    return render(request,'posts_by_category.html',context)


def blogs(request,blog_slug):
    single_blog = get_object_or_404(Blog,slug=blog_slug,status='Published')
    context = {'blog':single_blog}
    return render(request,'blogs.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter( Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) ,status='Published')
    context = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',context)