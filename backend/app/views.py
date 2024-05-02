from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserSerializer,
    RoleSerializer,
    AdminSerializer,
    ArticleSerializer,
    QuoteSerializer,
)
from .validations import custom_validation, validate_email, validate_password
from django.http.response import JsonResponse
from app.models import User, Role, Admin, Article, Quote

class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)

class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)

class UserApi(APIView):
    @staticmethod
    def get(request, id=0):
        if id != 0:
            user = User.objects.get(userId=id)
            user_serializer = UserSerializer(user)
            return JsonResponse(user_serializer.data, safe=False)
        else:
            users = User.objects.all()
            users_serializer = UserSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False)

    @staticmethod
    def post(request):
        user_data = request.data
        users_serializer = UserSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    @staticmethod
    def put(request):
        user_data = request.data
        user = User.objects.get(userId=user_data['userId'])
        users_serializer = UserSerializer(user, data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    @staticmethod
    def delete(request, id):
        user = User.objects.get(userId=id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)

class ArticleApi(APIView):
    @staticmethod
    def get(request, id=0):
        if id != 0:
            article = Article.objects.get(articleId=id)
            article_serializer = ArticleSerializer(article)
            return JsonResponse(article_serializer.data, safe=False)
        else:
            articles = Article.objects.all()
            articles_serializer = ArticleSerializer(articles, many=True)
            return JsonResponse(articles_serializer.data, safe=False)

    @staticmethod
    def post(request):
        article_data = request.data
        articles_serializer = ArticleSerializer(data=article_data)
        if articles_serializer.is_valid():
            articles_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    @staticmethod
    def put(request):
        article_data = request.data
        article = Article.objects.get(articleId=article_data['articleId'])
        articles_serializer = ArticleSerializer(article, data=article_data)
        if articles_serializer.is_valid():
            articles_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    @staticmethod
    def delete(request, id):
        article = Article.objects.get(articleId=id)
        article.delete()
        return JsonResponse("Deleted Successfully", safe=False)

class QuoteApi(APIView):
    @staticmethod
    def get(request, id=0):
        if id != 0:
            quote = Quote.objects.get(quoteId=id)
            quote_serializer = QuoteSerializer(quote)
            return JsonResponse(quote_serializer.data, safe=False)
        else:
            quotes = Quote.objects.all()
            quotes_serializer = QuoteSerializer(quotes, many=True)
            return JsonResponse(quotes_serializer.data, safe=False)

    @staticmethod
    def post(request):
        quote_data = request.data
        quotes_serializer = QuoteSerializer(data=quote_data)
        if quotes_serializer.is_valid():
            quotes_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    @staticmethod
    def put(request):
        quote_data = request.data
        quote = Quote.objects.get(quoteId=quote_data['quoteId'])
        quotes_serializer = QuoteSerializer(quote, data=quote_data)
        if quotes_serializer.is_valid():
            quotes_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    @staticmethod
    def delete(request, id):
        quote = Quote.objects.get(quoteId=id)
        quote.delete()
        return JsonResponse("Deleted Successfully", safe=False)
