from django.urls import path
from .views import (
    program_list, program_detail, create_program, 
    update_program, delete_program
)

app_name = 'programs'

urlpatterns = [
    path('', program_list, name='program_list'),
    path('<int:pk>/', program_detail, name='program_detail'),
    path('create/', create_program, name='create_program'),
    path('<int:pk>/edit/', update_program, name='update_program'),
    path('<int:pk>/delete/', delete_program, name='delete_program'),
]

