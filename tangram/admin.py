from django.contrib import admin

from .models import Unite


class UniteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'branche', 'theme_explogram', 'effectif')


admin.site.register(Unite, UniteAdmin)
