from django.shortcuts import get_object_or_404, redirect, render

from ..forms import BookForm
from ..models import Book


def book_list(request):
    books = Book.objects.all().order_by("title", "author")
    return render(request, "catalog/book_list.html", {"books": books})


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(
        request,
        "catalog/book_form.html",
        {"form": form, "form_title": "Add Book", "submit_label": "Create"},
    )


def book_update(request, pk: int):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(
        request,
        "catalog/book_form.html",
        {
            "form": form,
            "form_title": f"Edit Book: {book.title}",
            "submit_label": "Update",
        },
    )


def book_delete(request, pk: int):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "catalog/book_confirm_delete.html", {"book": book})

