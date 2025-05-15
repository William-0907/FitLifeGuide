from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {forms.PasswordInput()
    }