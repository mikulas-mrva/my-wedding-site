from django.contrib import admin

from .models import Visitor


class VisitorAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Hosté'
    verbose_name = 'Host'

    model = Visitor
    list_display = ('name', 'email')
    ordering = ('name',)


admin.site.register(Visitor, VisitorAdmin)
