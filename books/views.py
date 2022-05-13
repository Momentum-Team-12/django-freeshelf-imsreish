from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, User, Category
from .forms import BookForm, FavoriteForm

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {'books': books})


def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm()
    return render(request, "books/book_details.html", {'book': book, 'form': form, })


def add_book(request):
    if request.method == 'GET':
        form = FavoriteForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')

    return render(request, "books/add_book.html", {'form': form})


def add_favorite(request):
    if request.method == 'POST':
        form = FavoriteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='book_details')

    # return render(request, "books/book_details.html", {'form': form})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')

    return render(request, "books/edit_book.html", {
        'form': form,
        'book': book
    })


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='list_books')

    return render(request, "books/delete_book.html", {"book": book})


def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)

    return render(request, "books/category.html", {"books": books, "category": category})