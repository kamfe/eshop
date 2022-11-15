from django.shortcuts import render
from .models import ProcessorCharacteristics as PC
from django.core.paginator import Paginator
from cart.forms import CartAddProductForm

def index(request):
    proc_data = Paginator(PC.objects.all(), 30)
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

    if len(name_list) > 0:
        final_filter  = PC.core_filter(core_list) & PC.pack_filter(pack_list) & PC.name_filter(name_list)
    else:
        final_filter = PC.core_filter(core_list) & PC.pack_filter(pack_list)

    filtred_page = Paginator(final_filter, 1000).get_page(1)

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
    product = PC.objects.get(name__contains = product_name)
    cart_product_form = CartAddProductForm()

    data = {
        'product': product,
        'cart_product_form': cart_product_form,
        }
    return render(request, 'main/product_page.html', data)
