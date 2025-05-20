from django import forms
from .models import Profile,Post


class Register_form(forms.Form):
    username = forms.CharField(max_length=30,required=True)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(),required=True)
    password2= forms.CharField(max_length=30,widget=forms.PasswordInput(),label="Confirm Password")
    name = forms.CharField(max_length=30,required=False)
    age = forms.IntegerField(required=False)
    profile_picture = forms.FileField(widget=forms.FileInput(attrs={'type':'file'}),required=False)
    address = forms.CharField(max_length=30,required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows':3}),max_length=150,required=False)
    Dob = forms.DateField(widget=forms.DateInput(attrs={
        'type':'date'
    }),label="Your Date of birth :",required=False)
    
    email = forms.EmailField(max_length=50,required=False)
    mobile = forms.CharField(max_length=13,required=False)

    
    


class Login_form(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput())


class Add_and_update_post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title','post_file','post_description']

    post_title = forms.CharField(max_length=50)
    post_file = forms.FileField(max_length=400)
    post_description = forms.CharField(widget=forms.Textarea())