from django.db import models

# Create your models here.
class Task(models.Model):
    task_name=models.CharField(max_length=200)
    task_desc=models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now=True)
    completed=models.BooleanField(default=False)
    image=models.FileField(upload_to='Images/',default='Images/None/NO_img.jpg')
    def __str__(self):
        return self.task_name