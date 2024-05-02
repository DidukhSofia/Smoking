from rest_framework import serializers
from app.models import User, Role, Admin, Article, Quote

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'userName', 'birthday', 'email', 'password', 'startPrice', 'startAmount', 'progressDays', 'progressAmount', 'progressPrice', 'role')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'role')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'name', 'email', 'password', 'role')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('articleId', 'author', 'text')

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('quoteId', 'text')
