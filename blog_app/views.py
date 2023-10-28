from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from . models import Blog,Category,Comment
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
    
    if request.method == 'POST' :
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info) 
    
    comments = Comment.objects.filter(blog =single_blog)
    comments_count = comments.count
    
    context = {
        'blog':single_blog,
        'comments':comments,
        'comments_count':comments_count
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter( Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) ,status='Published')
    context = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',context)