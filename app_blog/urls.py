from django.urls import path, include
from . views import Index, About, DetailArticleView, LikeArticle, Featured, World, India, Technology, Design, Culture, Business, Politics, Opinion, Science, Style, Health, Travel, DeleteArticleView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('', About.as_view(), name='about'),
    path('tinymce/', include('tinymce.urls')),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article' ),
    path('<int:pk>/like',LikeArticle.as_view(), name = 'like_article'),
    path('featured/', Featured.as_view(), name='featured'),
    path('world/', World.as_view(), name='world'),
    path('india/', India.as_view(), name='india'),
    path('technology/', Technology.as_view(), name='technology'),
    path('design/', Design.as_view(), name='design'),
    path('culture/', Culture.as_view(), name='culture'),
    path('business/', Business.as_view(), name='business'),
    path('politics/', Politics.as_view(), name='politics'),
    path('opinion/', Opinion.as_view(), name='opinion'),
    path('science/', Science.as_view(), name='science'),
    path('style/', Style.as_view(), name='style'),
    path('health/', Health.as_view(), name='health'),
    path('travel/', Travel.as_view(), name='travel'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article'),
]
