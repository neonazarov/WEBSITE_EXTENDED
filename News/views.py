from django.shortcuts import render
from .models import *


# def index(request):
#     data = NewsModel.objects.all()
#     context = {
#         "items": data
#     }
#
#     return render(request, 'main/index.html', context)
def index(request):
    search_query = request.GET.get('search')
    if search_query:
        news = NewsModel.objects.filter(title__icontains=search_query)
    else:
        news = NewsModel.objects.order_by("-pk")[:8]

    return render(request, 'main/index.html', {'title': 'NEONews', 'news': news})


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')
