from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    # Additional fields for the custom user model
    phone_number = forms.CharField(max_length=20, required=False, help_text='Optional.')
    address = forms.CharField(widget=forms.Textarea, required=False, help_text='Optional.')
    street_address = forms.CharField(widget=forms.Textarea, required=False, help_text='Optional.')
    city = forms.CharField(widget=forms.Textarea, required=False, help_text='Optional.')
    state = forms.CharField(widget=forms.Textarea, required=False, help_text='Optional.')
    postal_code = forms.CharField(widget=forms.Textarea, required=False, help_text='Optional.')
    country = forms.CharField(widget=forms.Textarea, required=False, help_text='Optional.')
    user_type = forms.ChoiceField(choices=User.USER_GROUPS, initial='consumer')

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'address', 'user_type', 'password1','password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email address already exists.")
        return email

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User        
        fields = ['username','first_name','last_name', 'phone_number', 'email', 'address', 'date_joined', 'last_login']