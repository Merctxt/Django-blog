from django.contrib import admin
from django.urls import path
from blog.views import index, post, page

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:slug>/', post, name='post'),
    path('page/', page, name='page'),
]
