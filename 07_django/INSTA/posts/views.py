from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Image, HashTag
from .forms import PostModelForm, ImageModelForm, CommentModelForm
# from IPython import embed


@login_required()
@require_http_methods(['GET', 'POST'])
def create_post(request):
    if request.method == 'POST':
        post_form = PostModelForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()

            # create hashtag => <input name='tags' /> #hi #ssafy #20층
            content = post_form.cleaned_data.get('content')
            words = content.split(' ')
            for word in words:
                if word[0] == '#':
                    word = word[1:]
                    tag = HashTag.objects.get_or_create(content=word)
                    post.tags.add(tag[0])
                    # if tag[1]:
                    #     messages.add_message(request, messages.SUCCESS, f'{tag[0]}를(을) 처음 추가했습니다.')

            for image in request.FILES.getlist('file'):
                # embed()
                request.FILES['file'] = image
                # embed()
                image_form = ImageModelForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect('posts:post_list')
        else:
            pass
    else:
        post_form = PostModelForm()

    image_form = ImageModelForm()
    return render(request, 'posts/form.html', {
        'post_form': post_form,
        'image_form': image_form,
    })


@require_GET
def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html', {
        'posts': posts,
        'comment_form': comment_form,
    })


@login_required()
@require_POST
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_form = CommentModelForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
        return redirect('posts:post_list')
    # TODO: else => If comment is not valid?


@login_required()
@require_http_methods(['GET', 'POST'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user:
        if request.method == 'POST':
            post_form = PostModelForm(request.POST, instance=post)
            if post_form.is_valid():
                post_form.save()
                # update hashtag
                post.tags.clear()
                content = post_form.cleaned_data.get('content')
                words = content.split(' ')
                for word in words:
                    if word[0] == '#':
                        word = word[1:]
                        tag = HashTag.objects.get_or_create(content=word)
                        post.tags.add(tag[0])
                return redirect('posts:post_list')
        else:
            post_form = PostModelForm(instance=post)
    else:
        return redirect('posts:post_list')
    return render(request, 'posts/form.html', {
        'post_form': post_form
    })


@login_required()
@require_POST
def toggle_like(request, post_id):
    if request.is_ajax():
        user = request.user
        post = get_object_or_404(Post, pk=post_id)
        is_active = True
        # if post.like_users.filter(pk=user.id).exist():
        if user in post.like_users.all():
            post.like_users.remove(user)
            is_active = False
        else:
            post.like_users.add(user)
        return JsonResponse({'likeCount': post.like_users.count(),
                             'is_active': is_active,
                             })
    else:
        return HttpResponseBadRequest()


@require_GET
def tag_post_list(request, tag_name):
    tag = get_object_or_404(HashTag, content=tag_name)
    posts = tag.posts.all()
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html', {
        'posts': posts,
        'comment_form': comment_form,
        'h1': f'#{ tag } 를(을) 포함한 Posts 입니다.',
    })
