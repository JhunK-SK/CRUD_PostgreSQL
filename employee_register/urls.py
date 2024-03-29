from django.urls import path

from . import views

urlpatterns = [
    path('' , views.employee_list, name='list'),
    path('form/', views.employee_form, name='form'),
    path('<int:id>/', views.employee_form, name='edit'),
    path('delete/<int:id>/', views.employee_delete, name='delete'),
]