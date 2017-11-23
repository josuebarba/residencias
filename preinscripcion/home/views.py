# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .serializer import AlumnoMateriaInfoSerializer, EspecialidadSerializer, MateriaInfoSerializer, MateriaSerializer, AlumnoSerializer, AvanceMateriaSerializer
from .models import AlumnoMateriaInfo, Especialidad, MateriaInfo, Materia, Alumno, AvanceMateria
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
import xlrd
import os
# Create your views here.

def ReadXls(request):
    workbook = xlrd.open_workbook('ISC.xls', logfile=open(os.devnull, 'w'))
    worksheet = workbook.sheet_by_index(0)
    print worksheet.cell(0,0).value

class CountViewSet(viewsets.ModelViewSet):
    queryset = AlumnoMateriaInfo.objects.raw('Select home_materiainfo.id_materia, home_materiainfo.nombre, count(home_alumnomateriainfo.id_materia_id) as materia_count from home_materiainfo, home_alumnomateriainfo where home_materiainfo.id_materia = home_alumnomateriainfo.id_materia_id group by home_alumnomateriainfo.id_materia_id')
    serializer_class = AlumnoMateriaInfoSerializer

    def list(self,request):
        queryset = AlumnoMateriaInfo.objects.raw('Select home_alumnomateriainfo.id as id, home_materiainfo.nombre as nombre, count(home_alumnomateriainfo.id_materia_id) as cuenta from home_materiainfo, home_alumnomateriainfo where home_materiainfo.id_materia = home_alumnomateriainfo.id_materia_id group by home_alumnomateriainfo.id_materia_id')
        # queryset = AlumnoMateriaInfo.objects.all()
        serializer = AlumnoMateriaInfoSerializer(queryset, many=True)
        print serializer.data
        return Response(serializer.data)

class EspecialidadView(APIView):
    serializer_class = EspecialidadSerializer

    def get(self,request):
        especialidades = Especialidad.objects.all()
        response = self.serializer_class(especialidades,many=True)
        return Response(response.data)

class MateriaInfoView(APIView):
    serializer_class = MateriaInfoSerializer

    def get(self,request):
        materiasInfo = MateriaInfo.objects.all()
        response = self.serializer_class(materiasInfo,many=True)
        return Response(response.data)

class MateriaView(APIView):
    serializer_class = MateriaSerializer

    def get(self,request):
        materias = Materia.objects.all()
        response = self.serializer_class(materias,many=True)
        return Response(response.data)

class AlumnoView(APIView):
    serializer_class = AlumnoSerializer

    def get(self,request):
        alumnos = Alumno.objects.all()
        response = self.serializer_class(alumnos,many=True)
        return Response(response.data)

class AvanceMateriaView(APIView):
    serializer_class = AvanceMateriaSerializer

    def get(self,request):
        avance = AvanceMateria.objects.all()
        response = self.serializer_class(avance,many=True)
        return Response(response.data)
