# Generated by Django 5.0.1 on 2024-02-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogs', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='u_mail',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]