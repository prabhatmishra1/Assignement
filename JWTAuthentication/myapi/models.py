from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class College(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    total_course=models.PositiveIntegerField()
    total_student=models.PositiveIntegerField()
    link_university=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name