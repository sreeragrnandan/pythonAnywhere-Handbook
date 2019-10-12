from django.urls import path
from . import views
app_name = "contacts"
urlpatterns = [
    path('index/', views.contacts, name = 'contacts'),
    path('', views.newTemp, name = 'index')
]