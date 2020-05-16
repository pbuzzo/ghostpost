from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from myapp.models import PostInput
from myapp.forms import PostForm
from django.contrib import messages
import webbrowser as wb


def index(request):
    html = 'index.html'
    # Use .order_by()
    posts = PostInput.objects.all().order_by('-date')

    return render(
        request,
        html,
        {'posts': posts}
    )


def addpost(request):
    html = 'add_form.html'
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            PostInput.objects.create(
                title=data['title'],
                text=data['text'],
                post_type=data['post_type'],
            )
            messages.success(
                request,
                'Your password has been changed successfully!'
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = PostForm()

    return render(request, html, {'form': form})


def post_info(request, id):
    post = PostInput.objects.get(id=id)
    return render(
        request, "post_info.html",
        {"post": post}
    )


def upvote(request, id):
    post = PostInput.objects.filter(id=id).first()
    post.upvotes += 1
    post.save()

    return HttpResponseRedirect(reverse('homepage'))


def downvote(request, id):
    post = PostInput.objects.filter(id=id).first()
    post.downvotes += 1
    post.save()
    messages.success(request, 'Profile details updated.')

    return HttpResponseRedirect(reverse('homepage'))


def boast_posts(request):
    html = 'index.html'
    posts = PostInput.objects.all().order_by('-date')
    boasts = posts.filter(post_type=True)
    return render(
        request,
        html,
        {'boasts': boasts}
    )


def roast_posts(request):
    html = 'index.html'
    posts = PostInput.objects.all().order_by('-date')
    roasts = posts.filter(post_type=False)
    return render(
        request,
        html,
        {'roasts': roasts}
    )


def vote_posts(request):
    html = 'index.html'
    votes = PostInput.objects.all().order_by('-upvotes')
    return render(
        request,
        html,
        {'votes': votes}
    )


def posts_delete_view(request, id=None):

    post = get_object_or_404(PostInput, post_key=id)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post successfully deleted!")
        wb.open_new_tab('http://net-informations.com', new=2)
        return HttpResponseRedirect("/")

    posts = PostInput.objects.all().order_by('-date')

    return render(
        request,
        'post_info_del.html',
        {'posts': posts, 'was_successful': True}
    )
