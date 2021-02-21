from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class' : 'css_input'}))
    phone = forms.CharField(max_length=200)