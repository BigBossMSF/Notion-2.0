from django import forms
from .models import Notion

class NotionForm(forms.ModelForm):
    class Meta:
        model = Notion
        fields = ('title', 'text')


       # gjfdgdi