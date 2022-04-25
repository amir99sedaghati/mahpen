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
            # 'user_profile',
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

class UserUpdateForm(forms.ModelForm):
    # new_password = forms.CharField(max_length=128, min_length=8, required=False)
    # repeat_password = forms.CharField(max_length=128, min_length=8, required=False)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            # 'password',
            # 'user_profile',
        ]
        # widgets = {
        #     'password': forms.PasswordInput(),
        #     'new_password': forms.PasswordInput(),
        #     'repeat_password': forms.PasswordInput(),
        # }
    
    # def clean(self):
    #     super().clean()
    #     if self.cleaned_data['new_password'] != self.data.get('repeat_password') :
    #     # if self.data.get('new_password') != self.data.get('repeat_password') :
    #         raise forms.ValidationError('رمز های عبور باید مشابه یکدیگر باشند .')
    
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data['repeat_password'])
    #     if commit:
    #         user.save()
    #     user = authenticate(username=user.username, password=user.password)
    #     if user is not None :
    #         login(self.request, user)
    #     return user