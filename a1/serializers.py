from rest_framework import serializers,exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Question

class EmployeeSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=Question
        fields=(
            'title',
            'status',
            'created_by',
            'id',
            'image'

        )

class loginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):
        username=data.get("username","")
        password=data.get("password","")
        print(data)
        if(username and password):
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data["user"]=user
                else:
                    msg="deactive"
                    raise exceptions.ValidationError(msg)
            else:
                msg="wrong"
                raise exceptions.ValidationError(msg)
        else:
            msg="invalid"
            raise exceptions.ValidationError(msg)
        return data
