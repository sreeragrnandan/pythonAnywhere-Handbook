from django.urls import path
from . import views
app_name = "TimeTable"
urlpatterns = [
    path('', views.TimeTable, name = 'index')
]