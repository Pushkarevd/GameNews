from django.contrib import admin
from django.contrib.auth.models import User

from .models import StopGameHeadline, IgnHeadline, Comment, Comment_StopGame, Comment_IGN


class StopGameAdmin(admin.ModelAdmin):
    pass


class IgnAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'desc')


class UserAdmin(admin.ModelAdmin):
    fields = ('username', "email", 'user_permissions', 'is_active', 'last_login', 'groups', 'is_staff')
    readonly_fields = ('username', "email", 'is_active', 'last_login')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(StopGameHeadline, StopGameAdmin)
admin.site.register(IgnHeadline, IgnAdmin)
admin.site.register(Comment_StopGame)
admin.site.register(Comment_IGN)