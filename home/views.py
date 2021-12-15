from django.core import paginator
from django.shortcuts import render, redirect
from .form import *
from django.contrib import messages
from django.contrib.auth import logout
from django.core.paginator import Paginator


# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    blogs= BlogModels.objects.all().order_by('id')
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ui_blog.html',{'page_obj':page_obj})

def login_view(request):
    return render(request, 'login.html')



def blog_details(request, slug):
    context = {}
    try:
        blog_obj = BlogModels.objects.filter(slug = slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_details.html', context)

def see_blogs(request):
    context = {}
    try:
        blog_objss = BlogModels.objects.filter(user = request.user)
        
        context['blog_objss'] = blog_objss
    except Exception as e:
        print(e)
    return render(request, 'see_blogs.html', context)

def blog_delete(request, id):
    try:
        blog_obj = BlogModels.objects.get(id = id)
        if blog_obj.user == request.user:
            blog_obj.delete()
            
    except Exception as e:
        print(e)
    messages.info(request, 'Your blog has been deleted successfully!')
    return redirect('/see-blog')

def blog_update(request, slug):
    context = {}
    try:
        blog_obj = BlogModels.objects.get(slug = slug)
        
        if blog_obj.user != request.user:
            return redirect('/')
        initial_dict = {'content' : blog_obj.content}
        form = BlogForm(initial=initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            if form.is_valid():
                content = form.cleaned_data['content']
            BlogModels.objects.create(
                user = user, title = title, 
                content = content, image = image
            )
            messages.info(request, 'Your blog has been updated successfully!')
        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e:
        print(e)
    return render(request, 'update_blog.html', context)

def add_blog_view(request):
    context = {'form' : BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            if form.is_valid():
                content = form.cleaned_data['content']
            BlogModels.objects.create(
                user = user, title = title, 
                content = content, image = image
            )
            messages.info(request, 'Your blog has been added successfully!')
            return redirect('/add-blog')
        

    except Exception as e:
        print(e)
    return render(request, 'add_blog.html', context)

def register_view(request):
    return render(request, 'signin.html')

def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token= token)
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login')
    except Exception as e:
        print(e)
    return redirect('/')