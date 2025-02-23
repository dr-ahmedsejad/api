from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import status
# from .models import Article
# from .serializers import ArticleSerializer
#
# @api_view(['GET', 'POST'])
# def liste_articles(request):
#     if request.method == 'GET':
#         articles = Article.objects.all().order_by('-date_publication')
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def detail_article(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response({"error": "Article non trouvé"}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response({"message": "Article supprimé avec succès"}, status=status.HTTP_200_OK)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def detail_article(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response({"error": "Article non trouvé"}, status=status.HTTP_404_NOT_FOUND)
#
#     # Ajouter les groupes de l'utilisateur connecté dans la réponse
#     user_groups = request.user.groups.values_list('name', flat=True) if request.user.is_authenticated else []
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response({
#             "article": serializer.data,
#             "user_groups": list(user_groups),  # Inclure les groupes de l'utilisateur
#         })
#
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response({"message": "Article supprimé avec succès"}, status=status.HTTP_200_OK)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer, UserSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def liste_articles(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-date_publication')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detail_article(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response({"error": "Article non trouvé"}, status=status.HTTP_404_NOT_FOUND)

    # Récupérer les groupes de l'utilisateur connecté (l'utilisateur est authentifié)
    user_groups = request.user.groups.values_list('name', flat=True)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response({
            "article": serializer.data,
            "user_groups": list(user_groups),
        })

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response({"message": "Article supprimé avec succès"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)