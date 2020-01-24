from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from . models import Post, Category, Comment, Welcome, Menu
from django.views.generic.edit import CreateView
from django.utils.html import strip_tags
from django.db.models import Count
from django.urls import reverse


def mainview(request):
    menu_item_active = 1
    latest_posts = Post.objects.filter(kind='pst').order_by('-pub_date')[:10]
    menu_list = Menu.objects.all()
    categories = Category.objects.all()
    welcome_list = Welcome.objects.all()
    context = {
        'menu_item_active':menu_item_active,
        'latest_posts':latest_posts,
        'menu_list': menu_list,
        'categories':categories,
        'welcome_list':welcome_list,
    }
    return render(request, 'index.html', context)


def aboutview(request):
    menu_item_active = 2
    menu_list = Menu.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.filter(kind='abo')
    context = {
        'menu_item_active':menu_item_active,
        'posts':posts,
        'menu_list':menu_list,
        'categories':categories,
    }
    return render(request, 'about.html', context)

def contactview(request):
    menu_item_active = 3
    menu_list = Menu.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.filter(kind='con')
   
    context = {
        'menu_item_active':menu_item_active,
        'posts':posts,
        'menu_list':menu_list,
        'categories':categories,
    }
    return render(request, 'contacts.html', context)

def commentview(request):
    menu_item_active = 4
    menu_list = Menu.objects.all()
    categories = Category.objects.all()
    comments = Comment.objects.filter(status='pub').order_by('-pub_date')
    context = {
        'menu_item_active':menu_item_active,
        'menu_list':menu_list,
        'categories':categories,
        'comments':comments,
    }
    return render(request, 'comments.html', context)


def categoryview(request, slug):
    menu_item_active = 5
    menu_list = Menu.objects.all()
    categories = Category.objects.all()
    try:
        category_s = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category_s)
    except Category.DoesNotExist:
        category_s = ''
        post_list = ''
    context = {
        'menu_item_active':menu_item_active,
        'menu_list': menu_list,
        'category_s':category_s,
        'post_list':post_list,
        'categories':categories,
    }
    return render(request, 'category.html', context)


def leave_commentview(request):
    author = request.POST['author']
    author = strip_tags(author)
    text = request.POST['text']
    text = strip_tags(text)
    text = text[:1000]
    comment = Comment(author=author, text=text, status='pub')
    comment.save()
        
    context = {
        'comment':comment,
    }
    
    return redirect('posts:comments') 
    

def searchview(request):
    categories = Category.objects.all()
    text = request.POST['text']
    text = strip_tags(text)
    text = text[:20]
    warning = "Совет: Убедитесь что длина текста в поиске больше 3-х символов"
    if len(text)>3:
        posts = Post.objects.filter(text__icontains=text)
        qtt=len(posts)
    else:
        text = ''
        posts = ''
        qtt = 0
    context2 = {
        'categories':categories,
        'posts':posts,
        'warning':warning,
        'qtt':qtt,
    }
    return render(request, 'searchresult.html', context2)
