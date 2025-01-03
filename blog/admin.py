from django.contrib import admin

from .models import Post


class PostAdmin(Post):
    list_filter = ('status',)
    search_fields = ['title', 'text']

admin.site.register(Post)
