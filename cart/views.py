from django.shortcuts import render,get_object_or_404
from django.views import generic
from shop.models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse,reverse_lazy
from cart.models import Cart

class IndexView(generic.ListView):
    template_name = 'cart/cart_page.html'
    context_object_name='cart_product'

    def get_queryset(self):
        return Cart.objects.all()


class CartDelete(DeleteView):
    model = Cart
    success_url = reverse_lazy('cart:details')

def cart(request,prod_id):
    product_items = get_object_or_404(Product,pk=prod_id)
    cart_items = Cart(pr_id=product_items.pr_id, pr_logo=product_items.pr_logo,
        pr_title=product_items.pr_title, pr_price=product_items.pr_price, pr_offer=product_items.pr_offer)
    cart_items.save()
    cart_product = Cart.objects.all()
    return render(request, 'cart/cart_page.html', {'cart_product':cart_product})
