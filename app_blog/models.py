from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    featured = models.BooleanField(default=False)
    world = models.BooleanField(default=False)
    india = models.BooleanField(default=False)
    technology = models.BooleanField(default=False)
    design = models.BooleanField(default=False)
    culture = models.BooleanField(default=False)
    business = models.BooleanField(default=False)
    politics = models.BooleanField(default=False)
    opinion = models.BooleanField(default=False)
    science = models.BooleanField(default=False)
    health = models.BooleanField(default=False)
    style = models.BooleanField(default=False)
    travel = models.BooleanField(default=False)
    
    
class Comments(models.Model):
	post = models.ForeignKey(Article,related_name='comments', on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return '%s  - %s' %(self.post.title, self.name)
    