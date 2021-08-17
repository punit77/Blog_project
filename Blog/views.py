from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from Blog.models import Post, Category
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    # load all the posts from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)

    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats' : cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'posts.html', {'post': post,'cats': cats})

def category(request, url):

    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request,"category.html", {'cat':cat, 'posts': posts})


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')

        try:
            User.objects.create_user(username=username, password=password, email=email, first_name = name)
        except:
            messages.error(request, "Failed")
            return redirect('/')
        messages.success(request, "Registered Successfully")
        return redirect('/')

    return redirect('/')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect(reverse('Home'))

        messages.error(request,"Wrong username password")
        return redirect('/')
    return redirect('/')


def get_homepage(request):
    return render(request, 'homepage.html')

def logout_user(request):
    logout(request)
    return redirect("/")