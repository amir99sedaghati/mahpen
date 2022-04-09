from django import forms
from django.contrib.auth import get_user_model

class UserSignUpForm(forms.ModelForm):
    repeat_password = forms.CharField(max_length=128)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput(),
            'repeat_password': forms.PasswordInput(),
        }
    
    def clean(self):
        super().clean()
        if self.data.get('password') != self.data.get('repeat_password') :
            raise forms.ValidationError('Password 1 & 2 should be equal.')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        