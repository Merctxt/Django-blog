from django.db import models
from utils.rands import slugify_new
from django.contrib.auth.models import User

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55, unique=True, default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55, unique=True, default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Page(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField(max_length=55, unique=True, default=None, null=True, blank=True)
    content = models.TextField()
    is_published = models.BooleanField(default=True, help_text='Este campo precisará estar maracado para ser exibido no site')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)
        return super().save(*args, **kwargs)


    def __str__(self):
        return self.title
    

class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=75)
    slug = models.SlugField(max_length=55, unique=True, default=None, null=True, blank=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True, help_text='Este campo precisará estar maracado para ser exibido no site')
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='')
    cover_in_post_content = models.BooleanField(default=True, help_text='Este campo precisará estar maracado para que o imagem apareça no conteúdo do post')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='post_created_by', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='post_updated_by', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, default='')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title