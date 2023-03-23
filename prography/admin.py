from .models import Human

from django.contrib import admin


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'likes']
