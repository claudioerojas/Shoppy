from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Product

# Create your views here.
def hello_world(request):
    product = Product.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template = loader.get_template('product_detail.html')
    context = {
        'product': product
    }
    return HttpResponseRedirect(reverse('productos:product_detail', args=(product.pk)))
    #return HttpResponse(template.render(context, request))

