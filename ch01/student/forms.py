from django import forms
from django.core import validators
from student.models import Profile


#  form api

def start(value):
    if value[0] != 'A':
        raise forms.ValidationError('The length of name should be greater than 4')
    return value



class Registration(forms.Form):  # Use `forms.Form` for Form API (not `ModelForm`)
    name = forms.CharField(
        max_length=150,
        validators=[ 
            start,
            validators.MaxLengthValidator(5, message="Name cannot exceed 5 characters.")
        ],
        label="Enter_Name",
        error_messages={'required': 'Name Field is required'},
        widget=forms.TextInput(attrs={
            'class': 'text',
            'placeholder': 'Enter Name',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'text',
            'placeholder': 'Enter Password',
        }),
        label="Enter Password",
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'text',
            'placeholder': 'Confirm Password',
        }),
        validators=[
            validators.MinLengthValidator(4, message="Confirm password must be at least 4 characters long.")
        ],
        label="Confirm Password",
    )

    # Custom validation for matching passwords
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data






# // model form

# class Registration(forms.ModelForm):
#     confirm_password = forms.CharField(widget=forms.PasswordInput,validators=[validators.MinLengthValidator(4)])
#     class Meta:
#         model = Profile
#         fields = ['name','password']
#         labels = {'name':'Enter_Name','password':'Enter Password'}
#         error_messages = {
#             'name':{'required':'Name Field is required'}
#         }
#         widgets = {
#             'password':forms.PasswordInput(attrs={'class':'text','placeholder':'Enter Password'})
#         }
