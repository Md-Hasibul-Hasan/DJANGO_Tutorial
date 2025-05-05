from django import forms

# class Registration(forms.Form):
#     first_name=forms.CharField(
#         label='Full Name:',
#         # initial='First Name',
#         widget=forms.TextInput(
#             attrs={
#                 'class':'form-control',
#                 'placeholder':'First Name',
#             }
#         )
#     )
#     last_name=forms.CharField()
#     email=forms.EmailField()
#     password=forms.CharField(widget=forms.PasswordInput())
#     dob=forms.DateField()
#     time=forms.TimeField()
#     dt=forms.DateTimeField()
#     gender=forms.ChoiceField(
#         choices=[
#             ("M","male"),
#             ("F","female"),
#         ]
#     )
#     interests=forms.MultipleChoiceField(
#         choices=[
#             ("science","Science"),
#             ("art","Art"),
#             ("sport","Sport"),
#         ]
#     )


class Registration(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())