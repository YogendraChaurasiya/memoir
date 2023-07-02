from django.shortcuts import render, redirect
from django.views import View
from . forms import UserRegistrationForm
# from . forms import UserRegistrationForm, CommentForm
# from .models import Article

# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
            
        return render(request, 'users/register.html', {'form' : form})     
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')     
        
# def form_detail(self, request, *args, **kwargs):
#     post =  Article.objects.get(id=self.kwargs.get('pk'))
        
#     if request.method == "POST":
#         form = CommentForm(request.POST)
            
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             form.save()
#             return redirect('form_detail', id=post.id)
            
#     else:
#         form = CommentForm()
          
#     return render(request, 'app_blog/templates/blog/blog_post.html', {'post': post, 'form' : form})
    