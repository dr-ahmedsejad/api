from django.urls import path
from .views import liste_articles, detail_article

urlpatterns = [
    path('articles/', liste_articles, name='liste-articles'),
    path('articles/<int:pk>/', detail_article, name='detail-article'),
]

