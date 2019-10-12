from django.urls import path
from . import views
app_name = "administration"
urlpatterns = [
    path('', views.administration, name = 'index')
]