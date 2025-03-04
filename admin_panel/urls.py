from django.urls import path
from .views import admin_dashboard, admin_login, admin_logout

app_name = 'admin_panel'

urlpatterns = [
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin-login/', admin_login, name='admin_login'),
    path('admin-logout/', admin_logout, name='admin_logout'),
]
