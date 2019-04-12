from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('id', 'content', 'created_at', 'updated_at')
    list_display_links = ('id', 'content')


admin.site.register(Post, PostModelAdmin)
