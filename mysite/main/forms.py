from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
