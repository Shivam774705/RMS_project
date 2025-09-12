"""RMS_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from RMS_app.views import RmsAlarmCommonList 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('analytics/', views.analytics, name='analytics'),
    path('battery/', views.battery, name='battery'),
    path('useradmin/', views.useradmin, name='useradmin'),
    path('energy/', views.energy, name='energy'),
    path('grid_billing/', views.grid_billing, name='grid_billing'),
    path('filters/', views.filters, name='filters'),
    path('maps/', views.maps, name='maps'),
    path('status/', views.status, name='status'),
    path('reports/', views.reports, name='reports'),
    path('live_alarms/', views.live_alarms, name='live_alarms'),
    path('get_districts_for_filter/<str:state_id>/', views.get_districts_for_filter, name='get_districts_for_filter'),
    path('get_clusters_for_filter/<str:dist_id>/', views.get_clusters_for_filter, name='get_clusters_for_filter'),
    path('rovo_call/',views.rovo_call, name='rovo_call'),
    path('api/alarms/', RmsAlarmCommonList.as_view(), name='api-alarms-list'),
    # path('api/filter_alarms/', views.filter_alarms_api, name='filter-alarms-api'),

]
