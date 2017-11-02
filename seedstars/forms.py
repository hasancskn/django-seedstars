from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
	