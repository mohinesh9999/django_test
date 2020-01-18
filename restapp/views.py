from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,status
from .serializers import TaskSerializers,UserSerializer
from .models import Task
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework import filters
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
# Create your views here.
class CreateUserView(CreateAPIView):
    model=get_user_model()
    permission_classes=(AllowAny,)
    serializer_class=UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all().order_by('-date_created')
    serializer_class=TaskSerializers
    print(filters)
    filter_backends=(django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filter_fields=('completed',)
    ordering=('-date_created',)
    search_fields=('task_name',)
# class DueTaskViewSet(viewsets.ModelViewSet):
#     queryset=Task.objects.all().order_by('-date_created').filter(completed=False)
#     serializer_class=TaskSerializers
# class CompletedTaskViewSet(viewsets.ModelViewSet):
#     queryset=Task.objects.all().order_by('-date_created').filter(completed=True)
    # serializer_class=TaskSerializers
# class TaskList(viewsets.ModelViewSet):

#     serializer_class=TaskSerializers
#     def get_queryset(self, *args, **kwargs):
#         print(type(self),args)
#         tasks=Task.objects.all()
#         serializer=TaskSerializers(tasks,many=True)
#         print(serializer.data)
#         return(serializer.data) 