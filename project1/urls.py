"""
URL configuration for project1 project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myBlogs import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('contact',views.contact,name='contact'),
    path('subscription',views.subscription,name='subscription'),
    path('blog',views.blog,name='blog'),
    path('ck',views.ck,name='ck'),
    path('all_Blogs',views.all_Blogs,name='all_Blogs'), 
    # path('Blog_details',views.Blog_details,name='Blog_details'),
    path('Blog_details/<str:blog_id>/',views.Blog_details,name ='Blog_details'),
    path('login_user',views.login_user,name='login_user'),
    path('login_user',views.login_user,name='login_user'),
    path('signup_user',views.signup_user,name='signup_user'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('find_blog',views.find_blog,name='find_blog'),
    path('cat_blogs/<str:catagory>/',views.cat_Blogs,name ='cat_Blogs'),
    path('add_likes/<str:blog_id>',views.add_likes,name='add_likes'),
    path('comments/<str:blog_name>/',views.comments,name='comments'),
    path('add_comments',views.add_comments,name='add_comments'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        
