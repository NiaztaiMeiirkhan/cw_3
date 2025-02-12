from django.shortcuts import render, get_object_or_404
from .models import Thread, Post
from .forms import PostForm

def thread_detail(request, id):
    thread = get_object_or_404(Thread, pk=id)
    posts = Post.objects.filter(thread=thread)
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.thread = thread
        post.save()
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})
