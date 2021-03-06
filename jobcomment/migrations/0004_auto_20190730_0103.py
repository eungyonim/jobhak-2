# Generated by Django 2.2.2 on 2019-07-29 16:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobcomment', '0003_comment_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_author',
        ),
        migrations.AddField(
            model_name='blog',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
