from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class Blogger(models.Model):
    first_name = models.CharField(
        max_length=64,  null=True, help_text='Blogger first name')
    last_name = models.CharField(
        max_length=64, null=True, help_text='Blogger last name')
    slug = models.SlugField(max_length=128, null=True,
                            blank=True, db_index=True, help_text='for URL purposes')
    bio = models.TextField(max_length=2000, null=True, blank=True)
    blogs = models.ManyToManyField(
        'Blog', blank=True, help_text='blogs written by this author', editable=True, )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        # para ser usado no url, tendo como parâmetro o slug com o nome e sobrenome do blogueiro:
        return reverse('blogger_detail', args=[self.slug])


class Comment(models.Model):
    comment_author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    commentary = models.TextField(max_length=2000)

    def __str__(self):
        # mostra na página de comentários o nome do usuário e os primeiros 75 caracteres do comentário:
        return f'\nUser: {self.comment_author} | {self.commentary[:75].strip()}...'


class Blog(models.Model):
    title = models.CharField(max_length=100, help_text='Blog title')
    slug = models.SlugField(max_length=100, null=True, blank=True,
                            db_index=True, help_text='for URL purposes.')
    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=2000)
    comments = models.ManyToManyField(
        Comment, blank=True, help_text='comments for this post', editable=False)

    def __str__(self):
        return f'\n{self.title}'

    def get_absolute_url(self):
        # para ser usado no url, tendo como parâmetro o slug do blog:
        return reverse('blog_detail', args=[self.slug])
