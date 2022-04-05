from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditPostForm, ChoicesForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    #form_class = ChoicesForm
    template_name = 'home.html'
    ordering = ['-date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_dets.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


# def CategoryView(request, cats):
#     category_posts = Post.objects.filter(category=cats.replace('-', ' '))
#     return render(request, 'categories.html', 
#                     {   'cats': cats.title().replace('-', ' '),
#                         'category_posts': category_posts
#                         }
#                         )

class CategoryView(ListView):
    model = Post
    template_name = 'categories.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        post_by_cat = Post.objects.filter(category=self.kwargs['category'].replace('-', ' '))
        context = super(CategoryView, self).get_context_data(*args, **kwargs)

        context['category_posts'] = post_by_cat
        
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
