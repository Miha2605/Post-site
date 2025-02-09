from dbm.sqlite3 import DELETE_KEY

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import PostForm, CategoryForm


# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_detail.html"



class AddPostView(CreateView):
    model = Post
    template_name = "add_post.html"
    form_class = PostForm

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ('title', 'text')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'

def category_view(request, cats):
    category_posts = Post.objects.filter(category = cats)
    return render(request, "categories.html",{'cats':cats,'category_posts':category_posts})







