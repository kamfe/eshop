from django.shortcuts import render
from .models import ProcessorCharacteristics
from django.core.paginator import Paginator

def index(request):
    proc_data = Paginator(ProcessorCharacteristics.objects.all(), 30)
    page_number = request.GET.get('page')
    page_obj = proc_data.get_page(page_number)

    data = {
        'page_obj' : page_obj,
        'page_number': page_number,
    }

    return render(request, 'main/index.html', data)

def filtred(request):
    core_list = request.GET.getlist('filter_by_core')
    pack_list = request.GET.getlist('filter_by_pack')
    name_list = request.GET.getlist('filter_by_name')

    def core_filter(list):
        if len(list) == 0 or len(list) == 2:
            return ProcessorCharacteristics.objects.all()
        result = ProcessorCharacteristics.objects.filter(integrated_graphics_core__contains=list[-1])
        list.pop(-1)
        return result & core_filter(list)

    def pack_filter(list):
        if len(list) == 0 or len(list) == 2:
            return ProcessorCharacteristics.objects.all()
        result = ProcessorCharacteristics.objects.filter(name__contains=list[-1])
        list.pop(-1)
        return result & pack_filter(list)

    def name_filter(list):
        if len(list) == 0:
            return ProcessorCharacteristics.objects.filter(name__contains = 'None')
        result = ProcessorCharacteristics.objects.filter(name__contains=list[-1])
        list.pop(-1)
        return result | name_filter(list)

    if len(name_list) > 0:
        a  = core_filter(core_list) & pack_filter(pack_list) & name_filter(name_list)
    else:
        a = core_filter(core_list) & pack_filter(pack_list)

    filtred_page = Paginator(a, 1000).get_page(1)

    if len(filtred_page.object_list) == 0:
        is_empty = True
    else:
        is_empty = False

    data = {
        'filtred_page' : filtred_page,
        'is_empty' : is_empty,
    }

    return render(request, 'main/filtred.html', data)

def product_page(request, product_name:str):
    data = {
        'product_name': product_name,
    }
    return render(request, 'main/product_page.html', data)
