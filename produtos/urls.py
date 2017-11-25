from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from produtos import views

urlpatterns = [
            url(r'^produtos/$', views.produto_list),
            url(r'^produtos/(?P<pk>[0-9]+)$', views.produto_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
