from django.shortcuts import render,redirect
import time
from .forms import Register_form,Login_form,Add_and_update_post_form
from .models import Profile,Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.


def home_view(request):
    all_post = Post.objects.all().order_by('-post_created_at')

    data = {
        'title':'home_page',
        'all_post':all_post
    }
    return render(request,"home.html",data)


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        age = request.POST.get('age')
        profile_picture = request.FILES.get('profile_picture')
        address = request.POST.get('address')
        bio = request.POST.get('bio')
        Dob = request.POST.get('Dob')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please enter a different one.")
            return redirect('register')

        # Password validation
        if password != password2:
            messages.error(request, "Both passwords do not match. Please enter again.")
            return redirect('register')

        if len(password) < 9:
            messages.error(request, "Password must be more than 8 characters long.")
            return redirect('register')

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif not char.isalnum():
                has_special = True

        if not has_upper:
            messages.error(request, "Password must contain at least one uppercase letter.")
            return redirect('register')
        if not has_lower:
            messages.error(request, "Password must contain at least one lowercase letter.")
            return redirect('register')
        if not has_digit:
            messages.error(request, "Password must contain at least one number.")
            return redirect('register')
        if not has_special:
            messages.error(request, "Password must contain at least one special character.")
            return redirect('register')

        # All checks passed — create user
        user = User.objects.create(username=username)
        user.set_password(password)  # hash the password properly
        user.save()

        Profile(
            user=user,
            name=name,
            age=age,
            profile_picture=profile_picture,
            address=address,
            bio=bio,
            Dob=Dob,
            email=email,
            mobile=mobile
        ).save()

        return redirect('login')

    data = {
        'title': 'Registration page',
        'msg': 'Enter The Details Below',
        'form': Register_form(),
        'submit_btn': 'Register'
    }
    return render(request, "allform.html", data)

def login_view(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        messages.error(request,"incorrect username or password")
        return redirect('login')


    data = {
        'title':'Login page',
        'msg':'Enter The Details Below',
        'form':Login_form(),
        'submit_btn':'Login'
    }
    return render(request,"allform.html",data)


def add_post_view(request):
    
    if request.method=="POST":
        post_title = request.POST.get('post_title')
        post_file =request.FILES.get('post_file')
        post_description = request.POST.get('post_description')

        Post(
            profile=Profile.objects.get(user=request.user),
            post_title=post_title,
            post_description=post_description,
            post_file=post_file
        ).save()

        return redirect('home')
        

    data = {
        'title':'add post form',
        'msg':'add your new post',
        'form':Add_and_update_post_form(),
        'submit_btn':'Add_post',
    }
    return render(request,"allform.html",data)    


def update_profile_view(request):
    return render(request,"allform.html")


def update_post_view(request,id):
    post = Post.objects.get(id=id)
    if request.method=="POST":
        post_title = request.POST.get('post_title')
        post_file = request.FILES.get('post_file')
        post_description=request.POST.get('post_description')

        if post_file:
            post.post_file=post_file
        post.post_title=post_title
        post.post_description=post_description

        post.save()    
    data ={
        'title':'updatepost page',
        'msg':'update your post',
        'form':Add_and_update_post_form(instance=post),
        'submit_btn':'Update'
    }
    return render(request,"allform.html",data)


def logout_view(request):
    logout(request)
    return redirect('home')


def search_view(request):
    return render(request,"search.html")


def admin_panel_view(request):
    pass


def show_profile_view(request):
    profile_data = Profile.objects.get(user=request.user)
    profile_posts = Post.objects.filter(profile = profile_data)
    data = {
        'title':'profile page',
        'profile_data':profile_data,
        'profile_posts':profile_posts,
        'count_posts':len(profile_posts)
    }  
    return render(request,"profile.html",data)

def delete_post_view(request):
    return redirect('show_profile')



def other_profile_view(request,id):
    otherprofile = Profile.objects.get(id = id)
    if otherprofile == Profile.objects.get(user=request.user):
        return redirect('show_profile')
    
    otherpost = Post.objects.filter(profile = otherprofile)

    data = {
        'title':otherprofile.user.username,
        'profile_data':otherprofile,
        'profile_posts':otherpost,
        'count_posts':len(otherpost)
    }


    return render(request,"profile.html",data)


def post_detail_view(request,id):
    post = Post.objects.get(id = id)
    print(id)
    return render(request,"post_detail.html",{'post':post})





