
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import datetime

class Category(models.Model):
    name = models.CharField(max_length=150)
    category_slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    deleted_at = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.category_slug = slugify(self.name)
        super().save(*args,**kwargs)


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft","draft"),("published","published")
    )

    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="postsImage")
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    categories = models.ManyToManyField(Category,blank=True)
    deleted_at = models.DateTimeField(blank=True,null=True)
    created_at = models.DateTimeField(default=datetime.now(),blank=True)
    updated_at = models.DateTimeField(default=datetime.now(),blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="draft")

    def __str__(self):
        return f"{self.title}"

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args,**kwargs)
