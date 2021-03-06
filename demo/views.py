# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer, BookMiniSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)

# Create your views here.
# class Another(View):
    # books = Book.objects.all()
    # books = Book.objects.filter(is_published=True)
    # books = Book.objects.get(id=2) # gets one record only
    # output = ''
    # for book in books:
    #     output += f"we have {book.title} with ID {book.id} in db<br>"

    # output = f"we have {books.title} with ID {books.id} in db<br>"
    #
    # def get(self, request):
    #     return HttpResponse(self.output)


# def first(request):
#     books = Book.objects.all()
#     # return HttpResponse('first message')
#     return render(request, 'first_temp.html', {'books': books})
