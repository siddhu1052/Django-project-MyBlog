from django.contrib import admin
from .models import blog_category, contact_info, subscription_details, blog_post, comment
# Register your models here.

admin.site.register(blog_category)
admin.site.register(contact_info)
admin.site.register(subscription_details)
admin.site.register(blog_post)
admin.site.register(comment)