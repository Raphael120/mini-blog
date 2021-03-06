# Generated by Django 4.0.3 on 2022-03-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_blogger_slug_alter_blog_description_alter_blog_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger',
            name='blogs',
            field=models.ManyToManyField(blank=True, help_text='blogs written by this author', to='web.blog'),
        ),
    ]
