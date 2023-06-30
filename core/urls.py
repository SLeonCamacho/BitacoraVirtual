from django.urls import path
from . import views

urlpatterns = [
    path('ingresos/crear', views.vista_formulario, name="vista_formulario"),
    path('ingresos/', views.vista_lista, name="vista_list"),
    path('api/ingresos/', views.IngresoVistaLista.as_view(), name="lista_ingresos"),
    path('', views.login_view, name="vista_login"),
    path('logout', views.logout_view, name="vista_logout"),
]
