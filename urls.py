from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pagina_principal, name= 'pagina_principal'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('admin/', admin.site.urls),    # Agrega la URL de administración de Django
 
    
   
  

]
