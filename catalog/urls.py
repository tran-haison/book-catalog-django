from django.urls import path

from .controllers.books_controller import book_create, book_delete, book_list, book_update

urlpatterns = [
    path("", book_list, name="book_list"),
    path("books/new/", book_create, name="book_create"),
    path("books/<int:pk>/edit/", book_update, name="book_update"),
    path("books/<int:pk>/delete/", book_delete, name="book_delete"),
]

