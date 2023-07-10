from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from catalog.forms import BlogPostForm
from catalog.models import BlogPost


class BlogPostListView(generic.ListView):
    model = BlogPost
    template_name = 'catalog/blog/blogpost_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'catalog/blog/blogpost_detail.html'
    context_object_name = 'post'
    success_url = reverse_lazy('catalog:homepage')

    def get_queryset(self):
        return BlogPost.objects

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views_count += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class BlogPostCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'catalog/blog/blogpost_form.html'
    success_url = reverse_lazy('catalog:blog_post')
    permission_required = 'catalog.add_blogpost'
    # fields = ['title', 'content', 'preview', 'is_published']


class BlogPostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('catalog:blog_post')
    permission_required = 'catalog.change_blogpost'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class BlogPostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = BlogPost
    template_name = 'catalog/blog/blogpost_confirm_delete.html'
    permission_required = 'catalog.delete_blogpost'
    success_url = reverse_lazy('catalog:blog_post')