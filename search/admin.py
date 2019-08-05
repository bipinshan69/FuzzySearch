from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import WordBank
from .resources import WordBankResource

@admin.register(WordBank)
class WordBankAdmin(ImportExportModelAdmin):
    resource_class = WordBankResource
    list_display = ('word','frequency')