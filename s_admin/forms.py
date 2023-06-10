from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms


from s_admin.models import CustomUser, UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields= ("email",)
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)
        

# class LoginForm(forms.Form):
#     email = forms.EmailField(label='Email')
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

