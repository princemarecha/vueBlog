# Generated by Django 4.1.7 on 2023-03-29 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='thumbnails',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
