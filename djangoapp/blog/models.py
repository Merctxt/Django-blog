from django.db import models
from utils.rands import slugify_new

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