from django.urls import path
from cbtis128_app import views
urlpatterns = [
    path('',views.inicio_vista,name='inicio_vista'),
    path('registrarMateria/',views.registrarMateria,name='registrarMateria'),
    path("seleccionaMateria/<codigo>",views.seleccionaMateria,name="seleccionaMateria"),
     path('editarMateria/', views.editarMateria,name="editarMateria"),
    path('borrarMateria/<codigo>',views.borrarMateria, name="borrarMateria")

]