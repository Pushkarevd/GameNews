from django.contrib import admin

from .models import StopGameHeadline, IgnHeadline


class StopGameAdmin(admin.ModelAdmin):
    pass


class IgnAdmin(admin.ModelAdmin):
    pass


admin.site.register(StopGameHeadline, StopGameAdmin)
admin.site.register(IgnHeadline, IgnAdmin)
