from django.conf.urls import url
from . import views

app_name = 'productos'
urlpatterns = [
    url(r'^/$', views.hello_world, name='hello'),
    url(r'product/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail')
]