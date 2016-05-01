from django.conf.urls import url 
from price_App import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [ 
         	url(r'^api/price/(?P<pk>[0-9]+)$', views.product_price),
            url(r'^api/price_history/(?P<pk>[0-9]+)$', views.product_history),]   

urlpatterns = format_suffix_patterns(urlpatterns)

