from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password",)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def create_user(self, request):
        if self.is_valid():
            username = self.cleaned_data.get("username")
            password = self.cleaned_data.get("password")

            if request.user.is_authenticated:
                messages.add_message(request, messages.ERROR, 'You already have a account!')
                return False

            try:
                createUser = self.save()
                return True
            except Exception as e:
                print(e)
                return False

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )