from django.urls import path
from . import views as v

app_name = 'account'

urlpatterns=[
   path('register/', v.register, name='register'),
   path('login/', v.signIn, name='login'),
   path('logout/', v.singnOut, name='logout'),
]