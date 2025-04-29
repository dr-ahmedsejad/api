from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Article
from .serializers import ArticleSerializer, UitilisateurSerializer
from .pagination import ArticlePageNumberPagination, ArticleLimitOffsetPagination
from .permission import IsRedacteur, IsValidateur

@swagger_auto_schema(
    method='get',
    operation_id="Liste des articles",
    operation_description="Liste paginée des articles (réservée aux rédacteurs authentifiés)",
    responses={200: ArticleSerializer(many=True)},
)
@swagger_auto_schema(
    method='post',
    operation_id="Ajouter un articles",
    operation_description="Création d'un nouvel article (réservée aux rédacteurs authentifiés)",
    request_body=ArticleSerializer,
    responses={201: ArticleSerializer, 400: "Erreurs de validation"},
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IsRedacteur])
def liste_articles(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-date_publication')
        # Suite de traitement
        # Instanciation de la pagination
        paginator = ArticlePageNumberPagination()
        result_page = paginator.paginate_queryset(articles, request)
        # Sérialisation de la page paginée
        serializer = ArticleSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(
    method='get',
    operation_id="Récupérer un article par son id",
    operation_description="Récupérer les détails d’un article (réservée aux validateurs)",
    responses={200: ArticleSerializer, 404: "Article non trouvé"},
)
@swagger_auto_schema(
    method='put',
    operation_id="Modifier un article",
    operation_description="Mettre à jour un article (réservée aux validateurs)",
    request_body=ArticleSerializer,
    responses={200: ArticleSerializer, 400: "Erreurs de validation"},
)
@swagger_auto_schema(
    method='delete',
    operation_id="Supprimer un article",
    operation_description="Supprimer un article (réservée aux validateurs)",
    responses={200: "Article supprimé", 404: "Article non trouvé"},
)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsValidateur])
def detail_article(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response({"error": "Article non trouvé"}, status=status.HTTP_404_NOT_FOUND)
    # Suite de traitement
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response({"message": "Article supprimé avec succès"}, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='post',
    operation_id="Inscription",
    operation_description="Inscription d’un nouvel utilisateur",
    request_body=UitilisateurSerializer,
    responses={201: UitilisateurSerializer, 400: "Erreurs de validation"},
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UitilisateurSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
