from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import EmailPostForm,CommentForm
from django.core.mail import send_mail

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
    comments=post.comments.filter(active=True)

    new_comment=None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()            
    else:
        form = CommentForm()

    context={
        'post':post,
        'comments':comments,
        'form':form,
        'new_comment':new_comment,
    }
    return render(request,'blog/post_detail.html',context)

def sharePost(request,blog_slug):
    post=get_object_or_404(Post,slug=blog_slug,status='published')
    sent=False
    if request.method == 'POST':
        form=EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject='{} ({}) recommend you reading "{}"'.format(cd['name'],cd['email'],post.title)
            message='Read {} at {} \n\n {}\'s comments: {}'.format(post.title,post_url,cd['name'],cd['comments'])
            send_mail(subject,message,cd['email'],[cd['to']])
            sent=True
    else:
        form=EmailPostForm()        
    context={
        'form':form,
        'post':post,
        'sent':sent
    }
    return render(request,'blog/share.html',context)