from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Document.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'\'{title}\' is in use')
        return data
