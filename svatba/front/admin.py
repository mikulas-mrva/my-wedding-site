from django.contrib import admin

from .models import Message

class MessageAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Zprávy'
    verbose_name = 'Zpráva'
    model = Message
    list_display = ('sender', 'message')


admin.site.register(Message, MessageAdmin)
