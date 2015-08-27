from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': PasswordInput(render_value = True),
        }
