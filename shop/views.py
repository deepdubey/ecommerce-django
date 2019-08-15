from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from shop.models import Product

class IndexView(generic.ListView):
	template_name = 'shop/index.html'
	context_object_name = 'all_products'

	def get_queryset(self):
		return Product.objects.all()

class DetailView(generic.DetailView):
	model = Product
	template_name = 'shop/detail.html'
