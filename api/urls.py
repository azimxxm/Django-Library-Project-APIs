from django.urls import path
from .import views


urlpatterns = [
    path('books-list/', views.BookList, name='books-list'),
    path('books-detail/<str:pk>/', views.BookDetail, name='books-detail'),
    path('books-create/', views.BookCreate, name='books-create'),
    path('books-update/<str:pk>/', views.BookUpdate, name='books-update'),
    path('books-delete/<str:pk>/', views.BookDelete, name='books-delete'),
]
