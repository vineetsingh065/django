from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', required=True)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(help_text='Enter your message', label='Message', widget=forms.Textarea, required=True)
