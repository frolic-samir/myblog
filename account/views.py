from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import CreateUserForm

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
            print("User already exist")
   context = {
      'form':form,
   }
   return render(request,'account/register.html',context)

def signIn(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username=username, password=password)

      if user is not None:
         login(request,user)
         return redirect('blog:blog_list')
      else:
         print("Invalid username and password")
   return render(request,'account/login.html')

def singnOut(request):
   logout(request)
   return redirect('blog:blog_list')