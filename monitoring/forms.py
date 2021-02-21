from django import forms


class MakeRequestForm(forms.Form):
    link = forms.CharField()
    user = forms.CharField()
