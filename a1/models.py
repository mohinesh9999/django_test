from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    title=models.TextField(null=True,blank=False)
    status=models.CharField(max_length=10,default='inactive')
    created_by=models.ForeignKey(User,blank=True, null=True,on_delete=models.CASCADE)
    start_date=models.DateTimeField(blank=True, null=True)
    end_date=models.DateTimeField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.FileField(null=True,upload_to='Images/',default='Images/None/NO_img.jpg')

    def __str__(self):
        return self.title


