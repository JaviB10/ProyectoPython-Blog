# Generated by Django 4.2.7 on 2023-12-24 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='short_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
