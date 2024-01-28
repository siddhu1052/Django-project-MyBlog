from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import blog_category, contact_info, subscription_details, blog_post
from .forms import Blog_Form, BlogPost_Form
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate , login ,logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # return HttpResponse('<h1>this is the home page</h1>')
    #fetch the data from db
    x=blog_category.objects.all()
    # print (x)
    return render(request, 'myBlogs/home.html',{"category":x})

@login_required(login_url='login_user')
def contact(request):
    # return HttpResponse('<h1>this is the contact page</h1>')
    if request.method == 'GET':
        return render(request, 'myBlogs/contact.html')
    elif request.method == 'POST':
        email = request.POST.get('user_email')
        message = request.POST.get('message')
        x = contact_info(u_email=email, u_message=message)
        x.save()
        print(email)
        print(message)
        return render(request,'myBlogs/contact.html',{'feedback':'Your message has been recorded'})

def subscription(request):
    if request.method=='GET':
        return render(request,'myBlogs/subscription.html')
    elif request.method=='POST':
        user_email = request.POST.get('user_email')
        user_name=request.POST.get('user_name')
        user_package=request.POST.get('user_package')
        x=subscription_details(s_email=user_email, s_name=user_name, s_package=user_package)
        already_exists=subscription_details.objects.filter(s_email=user_email).exists();
        if already_exists:
            return render(request,'myBlogs/subscription.html',{'returned_message':'This Entry alaready exists'})
        else:
            x.save()
            return render(request,'myBlogs/subscription.html',{'returned_message':'Your Subscription has been confirmed'})

def blog(request):
    x = Blog_Form()  
    if request.method == "GET":
        return render(request,'myBlogs/blog.html',{"x":x})
    else:
        print("hi")
        form = Blog_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("hi")
            return redirect('home')
        else:
            return render(request,'myBlogs/blog.html',{"x":x})
        
def ck(request):
    x = BlogPost_Form()
    return render(request,'myBlogs/ck.html',{"x":x})

def all_Blogs(request):
    y=blog_post.objects.all();
    return render(request,'myBlogs/all_Blogs.html',{"y":y})
    
# def Blog_details(request,blog_id):
#     return render(request,'myBlogs/Blog_details.html'),

def Blog_details(request, blog_id):
    obj = get_object_or_404(blog_post, pk=blog_id)
    print(obj)
    print(blog_id)
    return render(request,'myblogs/blog_details.html', {"obj":obj})
    # return HttpResponse('blog_details')
    
def login_user(request):
    if request.method== 'GET':
        return render(request, 'myBlogs/login_user.html',{'form':AuthenticationForm()});
    else:
        a=request.POST.get('username')
        b=request.POST.get('password')
        user=authenticate(request,username=a,password=b)
        if user is None:
            return render(request,'myBlogs/login_user.html',{'form':AuthenticationForm(),'error':'Invalid credentials'})
        else :
            login(request, user)
            return redirect('home')
    
def signup_user(request):
    if request.method== 'GET':
        return render(request, 'myBlogs/signup_user.html',{'form':UserCreationForm()});
    else:
        print ('hello')
        a=request.POST.get('username')
        b=request.POST.get('password1')
        c=request.POST.get('password2')
        if b==c:
            if(User.objects.filter(username =a)):
                return render(request,'myBlogs/signup_user.html',{'form':UserCreationForm(),'error':'username already exists'})
            else:
                user=User.objects.create_user(username=a, password=b);
                user.save()
                login(request,user)
                return redirect('home')
        else:
            return render(request,'myBlogs/signup_user.html',{'form':UserCreationForm(),'error':'password mismatch'})
        
    
def logout_user(request):
    if request.method== 'GET':
        logout(request)
        return redirect('home');
    
    