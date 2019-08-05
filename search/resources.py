from import_export import resources
from .models import WordBank

class WordBankResource(resources.ModelResource):
    class Meta:
        model = WordBank
        import_id_fields = ['word']