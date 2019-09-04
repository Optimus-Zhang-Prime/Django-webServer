from django.contrib import admin
from .models import Post, User


class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'time', 'category', 'enable', 'del_pwd')
    ordering = ('-time',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'password', 'enable')


admin.site.register(Post, PostAdmin)
admin.site.register(User, UserAdmin)
