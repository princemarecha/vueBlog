# Generated by Django 4.1.7 on 2023-03-30 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_rename_thumbnails_blog_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='keywords',
            field=models.TextField(blank=True, null=True),
        ),
    ]
