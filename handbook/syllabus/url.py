from django.urls import path
from . import views
app_name = "syllabus"
urlpatterns = [
    path('', views.syllabus, name = 'index')
]