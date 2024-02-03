from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class blog_category(models.Model):
    blog_cat = models.CharField(max_length=60,unique=True)
    blogcat_img = models.ImageField(upload_to='images/')
    blogcat_description=models.TextField(max_length=200)
    def __str__(self):
        return self.blog_cat
    
class contact_info(models.Model):
    u_email = models.EmailField()
    u_message = models.TextField(max_length=200)
    def __str__(self):
        return self.u_email

class subscription_details(models.Model):
    s_email = models.EmailField()
    s_name=models.TextField(max_length=500)
    s_package = models.TextField(max_length=500)
    def __str__(self):
        return self.s_email

class blog_post(models.Model):
    blog_name =models.CharField(max_length=100)
    cover_img=models.ImageField(upload_to='images/')
    blog_description=RichTextField()
    like_count=models.IntegerField(default=0,null=True)
    views_count=models.IntegerField(default=0,null=True)
    Blog_cat=models.ForeignKey(blog_category,null=True, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.blog_name
    
class comment(models.Model):
    u_mail=models.EmailField(max_length=100, null=True, blank=False)
    comment=models.TextField(max_length=400,null=True,blank=False)
    Blog_name=models.ForeignKey(blog_post, null=True, default=True, on_delete=models.CASCADE)
    def __str_(self):
        return self.blog_name