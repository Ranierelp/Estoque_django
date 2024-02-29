from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    assunto = forms.CharField(label='Assunto')
    menssagem = forms.CharField(label='Menssagem', widget=forms.Textarea())

