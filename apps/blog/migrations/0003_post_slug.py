# Generated by Django 4.2.7 on 2023-12-01 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_autor_post_author_rename_titulo_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='default-slug', max_length=200),
        ),
    ]
