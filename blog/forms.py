from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super(EmailPostForm,self).__init__(*args,**kwargs)
        for fn,f in self.fields.items():
            f.widget.attrs['class']='form-control form-control-sm'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['body']
