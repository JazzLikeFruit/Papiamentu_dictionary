from django.urls import path
from dictionary import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('search/', views.search_engine, name='homepage'),
    path('word/<str:api_word>', views.word_api, name='homepage'),
]
