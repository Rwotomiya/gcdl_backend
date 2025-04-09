from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.views import ProduceViewSet, ProcurementViewSet, StockViewSet

router = DefaultRouter()
router.register('produce', ProduceViewSet)
router.register('procurements', ProcurementViewSet)
router.register('stock', StockViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', include('users.urls')),
    path('api/reports/', include('reports.urls')),
]

