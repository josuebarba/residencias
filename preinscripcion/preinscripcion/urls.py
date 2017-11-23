"""preinscripcion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from home import views

router = routers.DefaultRouter()
router.register(r'count',views.CountViewSet,base_name="asd")
# router.register(r'especialidades',views.EspecialidadView,base_name="especialidadview")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'especialidades/',views.EspecialidadView.as_view(),name='especialidad_view'),
    url(r'materiasInfo/',views.MateriaInfoView.as_view(),name='materiaInfo_view'),
    url(r'materias/',views.MateriaView.as_view(),name='materia_view'),
    url(r'alumnos/',views.AlumnoView.as_view(),name='alumno_view'),
    url(r'avance/',views.AvanceMateriaView.as_view(),name='avance_view'),
    url(r'read/',views.ReadXls,name='read')
]
