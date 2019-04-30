from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostModelForm


@login_required()
@require_http_methods(['GET', 'POST'])
def create_post(request):
    if request.method == 'POST':
        post_form = PostModelForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:posts_list')
    else:
        post_form = PostModelForm()
    return render(request, 'posts/form.html', {
        'post_form': post_form,
    })


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {
        'posts': posts,
    })


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    return render(request, 'posts/detail.html', {
        'post': post,
    })


@login_required()
@require_http_methods(['GET', 'POST'])
def update_post(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.user == request.user:
        if request.method == 'POST':
            post_form = PostModelForm(data=request.POST, instance=post)
            if post_form.is_valid():
                post_form.save()
                return redirect('posts:post_detail', post.pk)
        else:
            post_form = PostModelForm(instance=post)
    else:
        return redirect('posts:posts_list')
    return render(request, 'posts/form.html', {
        'post_form': post_form,
    })


@login_required()
@require_POST
def delete_post(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.user == request.user:
        post.delete()
    return redirect('posts:posts_list')


def toggle_like(request, post_pk):
    user = request.user
    post = get_object_or_404(Post, pk=post_pk)

    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)

    return redirect('posts:post_detail', post.pk)
