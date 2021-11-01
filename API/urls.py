from django.urls import path
from API import views

urlpatterns = [
    path('category/', views.Snippet.as_view(), name="category"),
    path('Tags/', views.Tags.as_view(), name="Tags"),
    ]