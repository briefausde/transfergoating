from django.contrib import admin
from django.urls import path
from farm.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FarmView.as_view(), name='farm_view'),
    path('herder/create/', HerderCreateView.as_view(), name='herder_create_view')
]
