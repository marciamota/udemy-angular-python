from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Book

# Create your views here.
class Another(View):
    # books = Book.objects.all()
    # books = Book.objects.filter(is_published=True)
    books = Book.objects.get(id=2) # gets one record only
    # output = ''
    # for book in books:
    #     output += f"we have {book.title} with ID {book.id} in db<br>"

    output = f"we have {books.title} with ID {books.id} in db<br>"

    def get(self, request):
        return HttpResponse(self.output)

def first(request):
    return HttpResponse('first message')