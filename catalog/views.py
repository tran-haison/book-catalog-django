"""
In this project we keep request-handling in `catalog.controllers.*` to emulate
an MVC separation (Django's MTV still requires view callables).
"""

from .controllers.books_controller import book_create, book_delete, book_list, book_update

__all__ = ["book_list", "book_create", "book_update", "book_delete"]
