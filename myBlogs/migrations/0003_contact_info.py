# Generated by Django 5.0.1 on 2024-01-16 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogs', '0002_blog_category_blogcat_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_email', models.EmailField(max_length=254)),
                ('u_message', models.CharField(max_length=200)),
            ],
        ),
    ]
