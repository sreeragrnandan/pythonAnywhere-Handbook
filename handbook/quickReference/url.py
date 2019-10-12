from django.urls import path
from . import views
app_name = "quickReference"
urlpatterns = [
    path('', views.index, name = 'index')
]