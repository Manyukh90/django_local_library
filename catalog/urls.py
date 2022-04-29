from django.urls import path
from . import views

urlpatterns = [
    # catalog/
    path('', views.index, name='index'),

    # catalog/books/
    path('books/', views.BookListView.as_view(), name='books'),

    # catalog/books/<id>
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

    # catalog/authors/
    path('authors/', views.AuthorListView.as_view(), name='authors'),

    # catalog/authors/<id>
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    # catalog/mybooks/
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

    # catalog/borrowed/
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),

    # catalog/book/<uuid:pk>/renew/
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

    # catalog/author/create/
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),

    # catalog/author/<int:pk>/update/
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),

    # catalog/author/<int:pk>/delete/
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),

    # catalog/book/create/
    path('book/create', views.BookCreate.as_view(), name='book-create'),

    # catalog/book/<int:pk>/update/
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    
    # catalog/book/<int:pk>/delete/
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]