from django.urls import re_path, path
from . import views


urlpatterns = [
    re_path(r'^create/$', views.order_create, name='order_create'),
    re_path(r'^created/(?P<order_id>\d+)/$', views.order_created, name='order_created')
]
