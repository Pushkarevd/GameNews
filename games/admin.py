from django.contrib import admin
from django.contrib.auth.models import User

from .models import StopGameHeadline, IgnHeadline


class StopGameAdmin(admin.ModelAdmin):
    fields = ('id', 'desc')


class IgnAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'desc')

class UserAdmin(admin.ModelAdmin):
    fields = ('username', "email", 'user_permissions', 'is_active', 'last_login', 'groups', 'is_staff')
    readonly_fields = ('username', "email", 'is_active', 'last_login')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(StopGameHeadline, StopGameAdmin)
admin.site.register(IgnHeadline, IgnAdmin)
