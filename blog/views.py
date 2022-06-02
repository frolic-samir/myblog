from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# from .forms import EmailPostForm
# from django.core.mail import send_mail

# Create your views here.

def post_list(request):
    object_list=Post.objects.all()
    paginator=Paginator(object_list,3) #No of post per page
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)

    context={
        'posts':posts,
        'page':page,
    }
    return render(request,'blog/post_list.html',context)

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,publish__year=year,publish__month=month,publish__day=day)
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('account:login')
        else:
            new_comment = request.POST.get('exampleFormControlTextarea1')
            Comment(post=post,user=User.objects.get(username=request.user),body=new_comment).save()

    comments=post.comments.filter(active=True)
    context={
        'post':post,
        'comments':comments,
    }
    return render(request,'blog/post_detail.html',context)

def searchContent(request):
    data = request.GET.get('q')
    search_posts = Post.objects.filter(title__icontains=data)
    paginator=Paginator(search_posts,3) #No of post per page
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)

    context={
        'posts':posts,
        'page':page,
    }
    return render(request, 'blog/search_content.html',context)

# def sharePost(request,blog_slug):
#     post=get_object_or_404(Post,slug=blog_slug,status='published')
#     sent=False
#     if request.method == 'POST':
#         form=EmailPostForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             post_url=request.build_absolute_uri(post.get_absolute_url())
#             subject='{} ({}) recommend you reading "{}"'.format(cd['name'],cd['email'],post.title)
#             message='Read {} at {} \n\n {}\'s comments: {}'.format(post.title,post_url,cd['name'],cd['comments'])
#             send_mail(subject,message,cd['email'],[cd['to']])
#             sent=True
#     else:
#         form=EmailPostForm()        
#     context={
#         'form':form,
#         'post':post,
#         'sent':sent
#     }
#     return render(request,'blog/share.html',context)