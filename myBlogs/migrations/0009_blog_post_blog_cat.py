# Generated by Django 5.0.1 on 2024-01-29 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogs', '0008_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='Blog_cat',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='myBlogs.blog_category'),
        ),
    ]
