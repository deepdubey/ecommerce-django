from django.conf.urls import url,include
from . import views

app_name= 'cart'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='details'),

    url(r'product/(?P<prod_id>[0-9]+)/add/$', views.cart, name='cart_update'),

    url(r'product/(?P<pk>[0-9]+)/delete/$', views.CartDelete.as_view(), name='cart_delete'),
]
