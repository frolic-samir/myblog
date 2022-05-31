from django.urls import path
from . import views as v

app_name = 'blog'

urlpatterns=[
    path('',v.post_list,name='blog_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',v.post_detail,name='blog_detail'),
    path('search/', v.searchContent, name='search_content')
]