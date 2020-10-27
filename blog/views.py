from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (DeleteView, UpdateView, TemplateView, CreateView, ListView, DetailView)
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#db queries u django dokumentaciji


class PostDetailView(DetailView):
    model = Post


#mixin login zahteva da je osoba ulogovana da bi kreirala post
#mixin idu sa class based views, dok sa function based views idu decoratori
class CreatePostView(LoginRequiredMixin, CreateView):

    login_url = '/login/'  #url na koji odlazi, gde odlazi ako nije ulogovan
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm

    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'  # url na koji odlazi, gde odlazi ako nije ulogovan
    redirect_field_name = 'blog/post_detail.html'  #
    form_class = PostForm

    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')



@login_required
def add_comment_to_post(request, pk): #pk je iz urla, to je pk od posta
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk= post.pk)

    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):

    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):

    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


@login_required
def post_publish(request, pk):

    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)