from typing import Any, Dict, Optional
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Article, Comments
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class Index(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/index.html'
    paginate_by = 1
    
class About(ListView):
    template_name = 'blog/about.html'

class Featured(ListView):
    model = Article
    queryset = Article.objects.filter(featured = True).order_by('-date')
    template_name = 'blog/featured.html'
    paginate_by = 1
    
class World(ListView):
    model = Article
    queryset = Article.objects.filter(world = True).order_by('-date')
    template_name = 'blog/world.html'
    paginate_by = 1
    
class India(ListView):
    model = Article
    queryset = Article.objects.filter(india = True).order_by('-date')
    template_name = 'blog/india.html'
    paginate_by = 1
    
class Technology(ListView):
    model = Article
    queryset = Article.objects.filter(technology = True).order_by('-date')
    template_name = 'blog/technology.html'
    paginate_by = 1
    
class Design(ListView):
    model = Article
    queryset = Article.objects.filter(design = True).order_by('-date')
    template_name = 'blog/design.html'
    paginate_by = 1
    
class Culture(ListView):
    model = Article
    queryset = Article.objects.filter(culture = True).order_by('-date')
    template_name = 'blog/culture.html'
    paginate_by = 1
    
class Business(ListView):
    model = Article
    queryset = Article.objects.filter(business = True).order_by('-date')
    template_name = 'blog/business.html'
    paginate_by = 1
    
class Politics(ListView):
    model = Article
    queryset = Article.objects.filter(politics = True).order_by('-date')
    template_name = 'blog/politics.html'
    paginate_by = 1
    
class Opinion(ListView):
    model = Article
    queryset = Article.objects.filter(opinion = True).order_by('-date')
    template_name = 'blog/opinion.html'
    paginate_by = 1
    
class Science(ListView):
    model = Article
    queryset = Article.objects.filter(science = True).order_by('-date')
    template_name = 'blog/science.html'
    paginate_by = 1
    
class Health(ListView):
    model = Article
    queryset = Article.objects.filter(health = True).order_by('-date')
    template_name = 'blog/health.html'
    paginate_by = 1
    
class Style(ListView):
    model = Article
    queryset = Article.objects.filter(style = True).order_by('-date')
    template_name = 'blog/style.html'
    paginate_by = 1
    
class Travel(ListView):
    model = Article
    queryset = Article.objects.filter(travel = True).order_by('-date')
    template_name = 'blog/travel.html'
    paginate_by = 1
    
class DetailArticleView(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailArticleView, self).get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        article = Article.objects.get(id=self.kwargs.get('pk'))
        if article.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        return context

class LikeArticle(View):
    def post(self, request, pk):
        article = Article.objects.get(id=pk)
        if article.likes.filter(pk=self.request.user.id).exists():
            article.likes.remove(request.user.id)
        else:
            article.likes.add(request.user.id)

        article.save()
        return redirect('detail_article', pk)
    
class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('index')
    
    def test_func(self):
        article = Article.objects.get(id=self.kwargs.get('pk'))
        return self.request.user.id == article.author.id

class AddCommentView(View):
    model = Comments
    template_name = 'add_category.html'
    fields = '__all__'