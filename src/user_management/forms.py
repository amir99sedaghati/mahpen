from django import forms
from django.contrib.auth import get_user_model

class UserSignUpForm(forms.ModelForm):
    repeat_password = forms.CharField(max_length=128)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'first_name',
            'last_name',
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
            raise forms.ValidationError('رمز های عبور باید مشابه یکدیگر باشند .')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        
class UserWalletForm(forms.Form):
    wallet = forms.IntegerField(
        min_value=1000,
    )