from django.urls import path
from .views import liste_articles, detail_article, register
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('register/', register, name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('articles/', liste_articles, name='liste-articles'),
    path('articles/<int:pk>/', detail_article, name='detail-article'),
]


