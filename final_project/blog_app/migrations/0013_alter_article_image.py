# Generated by Django 4.2.7 on 2023-12-24 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0012_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/article_images/'),
        ),
    ]
