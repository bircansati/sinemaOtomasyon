from django import forms
from django.contrib.auth import authenticate, login


class loginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)

    def clean(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        if username and password:
            user=authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('Kullanıcı adını veya parolayı yalnış girdiniz.')
        return super(loginForm,self).clean()