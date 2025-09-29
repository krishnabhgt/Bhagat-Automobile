from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', dashboard_home, name='dashboard-home'),
]