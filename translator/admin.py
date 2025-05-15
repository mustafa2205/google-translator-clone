from django.contrib import admin
from .models import Translation

# Register your models here.

@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ["source_text","translated_text","source_language","target_language","timestamp"]