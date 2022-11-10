from django.shortcuts import render
from .models import ProcessorCharacteristics
from django.core.paginator import Paginator

def index(request):
    proc_data = Paginator(ProcessorCharacteristics.objects.all(), 30)

    page_number = request.GET.get('page')
    page_obj = proc_data.get_page(page_number)

    data = {
        'page_obj' : page_obj,
        'page_number': int(page_number),
    }

    return render(request, 'main/index.html', data)
