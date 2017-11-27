from django.conf.urls import url, include
#from rest_framework.urlpatterns import format_suffix_patterns
from produtos import views
from rest_framework.routers import DefaultRouter
#from rest_framework.schemas import get_schema_view

router = DefaultRouter()
router.register(r'produtos', views.ProdutoViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'carrinhos', views.CarrinhoViewSet)
router.register(r'itemscarrinho', views.ItemCarrinhoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
