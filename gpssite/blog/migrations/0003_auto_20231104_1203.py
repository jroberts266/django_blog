# Generated by Django 3.2.22 on 2023-11-04 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='blog/files/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/images/'),
        ),
    ]
