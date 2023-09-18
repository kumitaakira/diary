from django import forms
from snippets.models import Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model=Snippet
        fields=('title','code','description')



from django import forms


tranz_zen_han=str.maketrans('−０１２３４５６７８９','-0123456789')

class ContactForm(forms.Form):
    tel=forms.CharField(label="電話番号")

    def clean_tel(self):
        tel=self.cleaned_data['tel']
        return tel.translate(tranz_zen_han)
    
    
