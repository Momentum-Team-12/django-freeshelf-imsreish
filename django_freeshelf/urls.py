"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books import views as books_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/login', books_views.book_details, name="login"),
    path('books/<slug:slug>', books_views.books_by_category, name="category"),
    path('', books_views.list_books, name='list_books'),
    path('books/<int:pk>/', books_views.book_details, name='book_details'),
    path('books/add', books_views.add_book, name='add_book'),
    path('books/<int:pk>/edit', books_views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete', books_views.delete_book, name='delete_book'),
]
