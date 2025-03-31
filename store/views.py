from django.views.generic import ListView

from .models import Product

class ProductViewList(ListView):
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    context_object_name = 'products'