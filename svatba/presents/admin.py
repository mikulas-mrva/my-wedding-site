from django.contrib import admin


from .models import Present, Person


class PresentAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Dary'
    verbose_name = 'Dar'

    model = Present
    # fields = ('username',)
    list_display = ('name', 'price', 'priority', 'is_taken', 'unlimited')
    # search_fields = ('username', 'customer__uid')
    ordering = ('priority',)
    exclude = ('slug',)


class PersonAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Darci'
    verbose_name = 'Darce'

    model = Person
    # fields = ('username',)
    list_display = ('email', 'present')
    # search_fields = ('username', 'customer__uid')
    ordering = ('present',)


admin.site.register(Present, PresentAdmin)
admin.site.register(Person, PersonAdmin)
