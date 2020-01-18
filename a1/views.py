from django.shortcuts import render
from rest_framework import viewsets,generics,mixins
from .serializers import EmployeeSerializer
from django.contrib.auth.models import User
from .models import Question
from .serializers import *
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.


class POOLListView(generics.GenericAPIView
    ,mixins.ListModelMixin
    ,mixins.CreateModelMixin
    ,mixins.RetrieveModelMixin
    ,mixins.UpdateModelMixin
    ,mixins.DestroyModelMixin):
    serializer_class=EmployeeSerializer
    queryset=Question.objects.all()
    lookup_field='id'
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated,IsAdminUser]
# ,SessionAuthentication,BasicAuthentication
    def get(self,request,id=None):
        print('delete1')
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)
    def post(self,request,id=None):
        return self.create(request)
    # def perform_create(self,serializer):
    def put(self,request,id=None):
        return self.update(request,id)
    def delete(self,request,id=None):
        print('delete')
        return self.destroy(request,id)
    def perform_update(self,serializer,id=None):
        print(self.request)
        serializer.save(created_by=self.request.user)
    def perform_create(self,serializer,id=None):
        serializer.save(created_by=self.request.user)



class POOLAPIView(APIView):
    def get(self,request):
        questions=Question.objects.all()
        serializer=EmployeeSerializer(questions,many=True)
        return Response(serializer.data,status=200)



class EmployeeViewSets(viewsets.ModelViewSet):
    print('hi')
    queryset=User.objects.all()
    serializer_class=EmployeeSerializer
@csrf_exempt
def poll(request):
    print(request)
    if(request.method=='GET'):
        questions=Question.objects.all()
        serializer=EmployeeSerializer(questions,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=EmployeeSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
def pool_details(request,id):
    try:
        instance=Question.objects.get(id=id)
    except Question.DoesNotExist as e:
        return JsonResponse({"error":"not exist"},status=400)
    if(request.method=="GET"):
        serializer=EmployeeSerializer(instance)
        return JsonResponse(serializer.data,status=200)

from rest_framework.views import APIView
from django.contrib.auth import login as django_login,logout as django_logout
from rest_framework.authtoken.models import Token

class loginView(APIView):
    def post(self,request):
        
        serializer=loginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data["user"]
        print(user,request,self)
        django_login(request,user)
        token,created=Token.objects.get_or_create(user=user)
        return Response({"token":token.key},status=200)




class logoutView(APIView):
    authentication_classes=(TokenAuthentication,)

    def post(self,request):
        django_logout(request)
        return Response(status=204)