from django.contrib import admin
from . import models


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",)
    }

    list_display = ('title', 'author', 'published', 'is_active')
    list_filter = ('author', 'published', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('title', 'short_description')
    ordering = ('-is_active', '-published')


admin.site.register(models.Article, ArticleAdmin)
