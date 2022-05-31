from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
   class Meta:
      model = User
      fields = ['email','password1','password2']
   
   def __init__(self,*args, **kwargs):
      super(UserCreationForm,self).__init__(*args,**kwargs)
      for fn, f in self.fields.items():
         f.widget.attrs['class']='form-control form-control-sm mt-1 mb-2'