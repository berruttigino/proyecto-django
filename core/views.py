from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostSearchForm


class PostListView(ListView):
    model = Post
    template_name = 'core/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.filter(publicado=True).order_by('-published_date')
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(title__icontains=q)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostSearchForm(self.request.GET or None)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'core/post_form.html'
    fields = ['title', 'content', 'author', 'tags', 'publicado']
    success_url = reverse_lazy('core:post-list')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'core/post_form.html'
    fields = ['title', 'content', 'author', 'tags', 'publicado']
    success_url = reverse_lazy('core:post-list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'core/post_confirm_delete.html'
    success_url = reverse_lazy('core:post-list')


# Vista que muestra únicamente los posts marcados como destacados y publicados
class PostFeaturedListView(ListView):
    model = Post
    template_name = 'core/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(publicado=True, featured=True).order_by('-published_date')