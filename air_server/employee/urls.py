from rest_framework import routers
from .api import EmployeeViewSet, EmployeeTempViewSet

router = routers.DefaultRouter()
router.register('api/employee', EmployeeViewSet, 'employee')
router.register('api/temperature', EmployeeTempViewSet, 'temperature')

urlpatterns = router.urls
