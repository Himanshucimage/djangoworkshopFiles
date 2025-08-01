from django.db import models

# Create your models here.

USER_TYPE = (
    ("Teacher", "Teacher"),
    ("Student", "Student"),
)

class lmsUser(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    number = models.BigIntegerField(unique=True)  
    password = models.CharField(max_length=20)
    userType = models.CharField(max_length=10, choices=USER_TYPE)

class courseUpload(models.Model):
    courseUploadId=models.AutoField(primary_key=True)
    courseName=models.CharField(max_length=20)
    courseDescription=models.CharField(max_length=50)
    createdAt=models.DateField()
    createdPlaylist=models.IntegerField()
    courseDuration=models.CharField(max_length=10)
    userName = models.ForeignKey(lmsUser, on_delete=models.CASCADE)
   
