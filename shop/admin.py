from django.contrib import admin
from .models import ProductModel, ProductTag, Category, BrandModel, SizeModel, ColorModel
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from .forms import ColorForms


@admin.register(ProductTag)
class Tag(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)



@admin.register(SizeModel)
class Size(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)


@admin.register(BrandModel)
class Brand(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)


@admin.register(ColorModel)
class Color(admin.ModelAdmin):
    list_display = ("code",)
    list_display_links = ("code",)
    search_fields = ("code",)
    form = ColorForms
    
    def color(self, obj):
        free_space = "&nbsp;" * 5
        return mark_safe(f"<div style='background-color:{obj.code}; width:200px;'>{free_space}</div>")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)


@admin.register(ProductModel)
class Product(admin.ModelAdmin):
    list_display = ("title", "price")
    list_display_links = ("title", "price")
    list_filter = ['created_at']
    search_fields = ("title", 'price')
    autocomplete_fields = ['category', 'tags', 'sizes', 'colors']
    readonly_fields = ['real_price', 'sale']


# class ProductAdmin(TranslationAdmin):
#     list_display = ("title", 'price', 'real_price', 'discount', 'created_at', 'sale')
#     list_display_links = ("title", 'price', 'created_at')
#     list_filter = ['created_at']
#     search_fields = ("title", 'price')
#     autocomplete_fields = ['category', 'tags', 'sizes', 'colors']
#     readonly_fields = ['real_price', 'sale']


#     class Media:
#         js = (
#             'modeltranslation/js/force_jquery.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }
    



# admin.site.register(ProductModel, ProductAdmin)


