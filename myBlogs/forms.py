from.models import blog_category,blog_post,comment
from django.forms import ModelForm
 


class Blog_Form(ModelForm):
    class Meta:
         model = blog_category
         fields = "__all__"

class BlogPost_Form(ModelForm):
    class Meta:
         model = blog_post
         fields = "__all__"
         
class add_comments_Form(ModelForm):
    class Meta:
        model= comment;
        # fields = {'comment'}
        fields = "__all__"