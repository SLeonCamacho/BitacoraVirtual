from django.urls import path
from . import views 

urlpatterns = [
    path('ingresos/', views.vista_formulario,name="vista_formulario"),
]
