from rest_framework import routers
from .api import EmployeeViewSet, TemperatureViewSet, EmployeeTempViewSet

router = routers.DefaultRouter()
router.register('api/employee', EmployeeViewSet, 'employee')
router.register('api/temperature', TemperatureViewSet, 'temperature')
router.register('api/empTemp', EmployeeTempViewSet, 'empTemp')

urlpatterns = router.urls
