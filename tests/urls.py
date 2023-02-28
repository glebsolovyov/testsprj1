from django.urls import path
from .views import *

urlpatterns = [
    path('', tests_list_view, name='tests_list_url'),
    path('create', TestCreate.as_view(), name='test_create_url'),
    path('solution', TestSolution.as_view(), name='test_solution_url'),
    path('check', check_test, name='check_test')
]