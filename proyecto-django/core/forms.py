from django import forms

class PostSearchForm(forms.Form):
    q = forms.CharField(
        label='Buscar',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Buscar por título...'})
    )