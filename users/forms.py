from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    DROPDOWN = (
        ('1', '1 BTC'),
        ('2', '2 BTC'),
        ('3', '3 BTC'),
        ('4', '4 BTC'),
        ('5', '5 BTC'),
        ('6', '6 BTC'),
        ('7', '7 BTC'),
        ('8', '8 BTC'),
        ('9', '9 BTC'),
        ('10', '10 BTC'),
    )

    email = forms.EmailField()
    wallet = forms.ChoiceField(choices=DROPDOWN)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['wallet'].label = "How many BTC you want to deposit?"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'wallet']
        labels = {
            "wallet": "boh"
        }