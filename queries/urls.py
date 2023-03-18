from django.urls import path
from .views import solve_question

urlpatterns = [
    path('', solve_question, name='math_query')
]