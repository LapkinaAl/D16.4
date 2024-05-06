from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, verbose_name='Author')
    rating = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['id', 'user_id']

class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True, verbose_name='Category')
    #subscribers = models.ManyToManyField(User, null=True, blank=True, related_name='categories')
    subscribers = models.ManyToManyField(User, through='CategorySubscriber')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

class CategorySubscriber(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):
    article = 'AR'
    news = 'NE'

    CONTENT = [
        (article, 'Article'),
        (news, 'News'),
    ]
    post_content = models.CharField(max_length=2,
                                    choices=CONTENT,
                                    default=article)
    post_time_in = models.DateTimeField(auto_now_add=True)
    post_name = models.CharField(max_length=255)
    post_text = models.CharField(max_length=10000)
    post_author = models.ForeignKey(Author,
                                    to_field='user_id',
                                    on_delete=models.CASCADE,
                                    verbose_name='Author')
    post_category = models.ManyToManyField(Category, through='PostCategory')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['post_name']

    def preview(self):
        return self.post_text[0:125] + '...'

    def __str__(self):
        return f'{self.post_name}: {self.post_text[:15]}: {self.post_author}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')

class Comment(models.Model):
    comment_text = models.TextField()
    comment_time_in = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
