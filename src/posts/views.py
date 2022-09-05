from multiprocessing import context
from operator import imod
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post, Photo

def index(request):
    latest_post=Post.objects.order_by('-date')[0:1]
    latest_photo=Photo.objects.order_by('-date')[0:4]
    context={
        'latest_post': latest_post,
        'latest_photo': latest_photo,
    }
    return render(request, 'index.html', context)

def aboutme(request):
    return render(request, 'aboutme.html', {})

def posts(request):
    post_list=Post.objects.order_by('-date')
    paginator=Paginator(post_list, 4)
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset=paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)   
    context={
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'posts.html', context)

def photos(request):
    photo_list=Photo.objects.order_by('-date')
    paginator=Paginator(photo_list, 4)
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset=paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)   
    context={
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'photos.html', context)
def post(request, id):
    post=get_object_or_404(Post, id=id)
    context={
        'post': post,
    }
    return render(request, 'post.html', context) 