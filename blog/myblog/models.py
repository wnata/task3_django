from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django.utils.text import slugify



class Category(models.Model):
    CATEGORY_CHOICES = (
        ('coding', 'coding'),
        ('coding', 'sports'),
        ('coding', 'life'),
    )
    name = models.CharField(max_length=255, choices = CATEGORY_CHOICES)
    
    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(default=now, editable=False)
    category = models.CharField(max_length=255, default='uncategorized')
    slug_category = models.SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.title} | {str(self.author)}'

    def save(self, *args, **kwargs):
        if not self.slug_category:
            self.slug_category = slugify(self.category)

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        #return reverse("article-detail", args=(str(self.id)) )
        return reverse("home")
