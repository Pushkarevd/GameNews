from django.contrib import admin

from .models import StopGameHeadline, IgnHeadline


class StopGameAdmin(admin.ModelAdmin):
    fields = ('id', 'desc')


class IgnAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'desc')


admin.site.register(StopGameHeadline, StopGameAdmin)
admin.site.register(IgnHeadline, IgnAdmin)
