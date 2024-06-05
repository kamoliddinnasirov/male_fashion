from django.contrib import admin
from pages.models import Contact, Banner, MainSMImage, MainSM


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_display_links = ['name', 'email']
    search_fields = ['name', 'email', 'message']
    list_filter = ['created_at']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'collection', 'is_active']
    list_display_links = ['title', 'collection']
    search_fields = ['title', 'collection']
    list_filter = ['created_at']


@admin.register(MainSM)
class MainSMAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'tag']
    list_display_links = ['title', 'description', 'tag']


@admin.register(MainSMImage)
class MainAdmin(admin.ModelAdmin):
    list_display = ['image']