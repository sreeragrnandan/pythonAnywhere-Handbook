from django.db import models
from multiselectfield import MultiSelectField
import pymysql
# Create your models here.
class comity(models.Model):
    comity_name = models.CharField(max_length=200)
    def __str__(self):
        return self.comity_name
    def __str__(self):
        return '' + self.comity_name

class Member(models.Model):
    DEPARTMENT_CHOICES = (
        ('CSE','CSE'),('ECE','ECE'),('Administration','Administration'),('CIVIL','CIVIL')
        ,('EEE','EEE'),('ME','ME'),('BSH','BSH'),('Office','Office'),('Library','Library'),
        ('COMPUTER CENTER','COMPUTER CENTER'),('HOSTEL','HOSTEL'),
    )
    comity = models.ForeignKey(comity, on_delete=models.CASCADE)
    jecc_code = models.CharField(max_length=100,default='JEC')
    Member_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length = 80,choices = DEPARTMENT_CHOICES)
