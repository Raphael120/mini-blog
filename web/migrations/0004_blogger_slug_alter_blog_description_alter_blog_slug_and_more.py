# Generated by Django 4.0.3 on 2022-03-17 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger',
            name='slug',
            field=models.SlugField(blank=True, help_text='for URL purposes', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, help_text='for URL purposes.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blogger',
            name='bio',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentary',
            field=models.TextField(max_length=2000),
        ),
    ]
