from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post

class PostListView(generic.ListView):
    # template_name = 'app/post_confirm_delete.html'
    context_object_name = 'posts'
    model = Post

class PostDetailView(generic.DetailView):
    # template_name = 'app/post_detail.html'
    model = Post

class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    # template_name = 'app/post_delete.html'
    model = Post
    success_url = reverse_lazy('post-list')

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    # template_name = 'app/post_form.html'
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
