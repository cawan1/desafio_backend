from django.conf.urls import url, include
#from rest_framework.urlpatterns import format_suffix_patterns
from carrinho import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'carrinho', views.CarrinhoViewSet)
router.register(r'itemcarrinho', views.ItemCarrinhoViewSet)


urlpatterns = [
        url(r'^', include(router.urls)),
        ]


#urlpatterns = [
#        url(r'^carrinho/$', views.carrinho_list),
#        url(r'^carrinho/(?P<pk>[0-9]+)$', views.item_carrinho_list),
#]
#
#urlpatterns = format_suffix_patterns(urlpatterns)

