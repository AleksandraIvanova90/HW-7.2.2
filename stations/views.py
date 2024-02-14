import csv


from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))

with open(f'{BUS_STATION_CSV}', encoding="UTF-8") as f:
    data = list(csv.DictReader(f))

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(data, per_page=10)
    page = paginator.get_page(page_number)
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

