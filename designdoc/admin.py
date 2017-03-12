#encoding=utf-8
from django.contrib import admin

from .models import Document
# Register your models here.


class DocumentAdmin(admin.ModelAdmin):
    search_fields = ('risk',)
admin.site.register(Document, DocumentAdmin)
