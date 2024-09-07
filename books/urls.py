from django.urls import path

from books import views
app_name = 'books'

urlpatterns = [
    path('<slug:genre_slug>/', views.catalog, name='index'),
    path('book/<slug:book_slug>/', views.book, name='book'),
]