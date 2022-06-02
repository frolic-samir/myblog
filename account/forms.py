import email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
   email = forms.EmailField() 
   class Meta:
      model = User
      fields = ['email','password1','password2']
   
   def __init__(self,*args, **kwargs):
      super(UserCreationForm,self).__init__(*args,**kwargs)
      for fn, f in self.fields.items():
         f.widget.attrs['class']='form-control form-control-sm mt-1 mb-2'


class LoginForm(forms.Form):
   email =  forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-sm'}))
   password =  forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))