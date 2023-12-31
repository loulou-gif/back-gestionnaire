"""
URL configuration for stream project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gestionnaire.views import StockViewSet, DirectionViewSet, UserViewSet, LocationViewSet, statusProductViewSet, categorieStockViewSet, UserListViewSet
from rest_framework import routers
from . import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'stock',viewset=StockViewSet)
# router.register(r'user',viewset=UserDetailViewSet, basename='user-detail')
router.register(r'direction',viewset=DirectionViewSet)
router.register(r'create-user',viewset=UserViewSet)
router.register(r'Emplacement',viewset=LocationViewSet)
router.register(r'status-produit',viewset=statusProductViewSet)
router.register(r'categories-produits',viewset=categorieStockViewSet)
router.register(r'list-user',viewset=UserListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    # path('api/', include('gestionnaire.urls')),  # Include the app's URLs
    path('',include(router.urls))
]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)