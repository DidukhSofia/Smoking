from django.urls import path
from app import views

urlpatterns = [
    path('register', views.UserRegister.as_view(), name='register'),
	path('login', views.UserLogin.as_view(), name='login'),
	path('logout', views.UserLogout.as_view(), name='logout'),
    path('user/', views.UserApi.as_view()),
    path('user/<int:id>/', views.UserApi.as_view()),
    
    path('article/', views.ArticleApi.as_view()),
    path('article/<int:id>/', views.ArticleApi.as_view()),

    path('quote/', views.QuoteApi.as_view()),
    path('quote/<int:id>/', views.QuoteApi.as_view()),
]
