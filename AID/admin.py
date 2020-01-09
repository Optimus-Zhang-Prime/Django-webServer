from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TrainActivity
from users.models import User

# Register your models here.
class TrainActivityAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'description', 'createDate', 'enable', 'isAttest')


admin.site.register(TrainActivity, TrainActivityAdmin)
#admin.site.register(User, UserAdmin)
