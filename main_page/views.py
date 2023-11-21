# from typing import Any
#
# from django.shortcuts import render, get_object_or_404
# from .models import FilmModel, Afisha, Slider
#
# #не полное отображение
# def book_list_view(request):
#     if request.method == 'GET':
#         book_list = BookModel.objects.all()
#         afisha_list = Afisha.objects.all()
#         slider_list = Slider.objects.all()
#         return render(request, template_name='books/index.html', context={
#             'book_list': book_list,
#             'afisha_list': afisha_list,
#             'slider_list': slider_list
#         })
#
# #detail
# def book_detail_view(request, id):
#     if request.method == 'GET':
#         book_id: Any = get_object_or_404(BookModel, id=id)
#         return render(request, template_name='books/book_detail.html', context={'book_id': book_id})

from django.shortcuts import render, get_object_or_404
from .models import FilmModel, Afisha, Slider

#не полное отображение
def film_list_view(request):
    if request.method == 'GET':
        film_list = FilmModel.objects.all()
        afisha_list = Afisha.objects.all()
        slider_list = Slider.objects.all()
        return render(request, template_name='films/index.html', context={
            'film_list': film_list,
            'afisha_list': afisha_list,
            'slider_list': slider_list
        })

#detail
def film_detail_view(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(FilmModel, id=id)
        return render(request, template_name='films/film_detail.html', context={'film_id': film_id})