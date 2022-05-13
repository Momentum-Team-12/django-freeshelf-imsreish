from django import forms
from .models import Book, User, Favorite


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 
            'author',
            'category',
            'description',
        ]


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = [
            'book',
            'user',
        ]