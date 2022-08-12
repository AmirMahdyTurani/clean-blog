from django.contrib import admin
from . import models
from django.utils.translation import ngettext
from django.contrib import messages


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
    actions = ['is_active_to_false']
    empty_value_display = '-خالی-'

    @admin.action(description="غیر فعال کردن پست های انتخاب شده")
    def is_active_to_false(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, ngettext(
            '%d مقاله غیر فعال شدند',
            '%d مقالات غیر فعال شدند.',
            updated
        ) % updated, messages.SUCCESS)


admin.site.register(models.Article, ArticleAdmin)
