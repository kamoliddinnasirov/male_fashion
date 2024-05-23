from django.contrib import admin
from blog.models import Post, PostTag, Comment, Author

@admin.register(PostTag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_display_links = ['title']
    list_filter = ['created_at']
    search_fields = ['title', 'body']
    autocomplete_fields = ['author', 'tag']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_display_links = ['full_name']
    search_fields = ['full_name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    list_display_links = ['name', 'email', 'phone']
    list_filter = ['created_at']