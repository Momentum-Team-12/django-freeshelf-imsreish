from django import forms
from .models import Book, User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 
            'author',
            'category',
        ]