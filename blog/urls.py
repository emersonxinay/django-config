from django.urls import path
from blog import views
urlpatterns = [
  path('', views.index),
  path('hola/<str:usuario>/', views.hola),
  path('nosotros/', views.nosotros),
  path('tarea/<int:id>/', views.taks)
]