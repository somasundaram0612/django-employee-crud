from django.urls import path
from . import api_views

urlpatterns = [
    path('employees/', api_views.employee_list_create, name='employee-list-create'),
    path('employees/<int:id>/', api_views.employee_detail, name='employee-detail'),
]
