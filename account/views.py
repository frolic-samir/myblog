from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import CreateUserForm, LoginForm
from django.contrib import messages

# Create your views here.

def register(request):
   form = CreateUserForm()
   if request.method == 'POST':
      form= CreateUserForm(request.POST)
      if form.is_valid():
         if not User.objects.filter(username=form.cleaned_data['email']).first():
            f=form.save(commit=False)
            f.username =form.cleaned_data['email']
            f.save()         
            print("Account created.")
            return redirect('account:login')
         else:
            messages.info(request,"User already exist")
   context = {
      'form':form,
   }
   return render(request,'account/register.html',context)

def signIn(request):
   form = LoginForm(request.POST or None)
   if form.is_valid():
      f=form.cleaned_data
      user = authenticate(username=f['email'], password=f['password'])

      if user is not None:
         login(request,user)
         return redirect('blog:blog_list')
      else:
         messages.info(request,"Invalid user")
   context = {
      'form': form
   }
   return render(request,'account/login.html', context)

def singnOut(request):
   logout(request)
   return redirect('blog:blog_list')