# Generated by Django 4.1.7 on 2023-03-30 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_alter_blog_author_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='authorId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogger', to=settings.AUTH_USER_MODEL),
        ),
    ]
