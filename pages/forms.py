from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='User Name', min_length=4, max_length=8)
    password = forms.CharField(label='Password', min_length=4, max_length=64, widget=forms.PasswordInput()) 
