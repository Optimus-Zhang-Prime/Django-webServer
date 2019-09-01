from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'time', 'category', 'enable', 'del_pwd')
    ordering = ('-time',)


admin.site.register(Post, PostAdmin)
