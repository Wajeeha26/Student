from django.db import models
from django.db import models
#from django.db.models.signals import post_save
#from django.dispatch import receiver
from cloudinary.models import CloudinaryField

class Course(models.Model):
    course = models.CharField(max_length=50, unique=True)

class Student(models.Model):
    student_name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    address = models.TextField()
    date_of_birth = models.DateField()
    reg_no = models.IntegerField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.IntegerField()
    Degree = models.CharField(max_length=50)
    Student_image = models.FileField(upload_to="media/",max_length=1000,null=True,default=None)
    Student_image_NEW = CloudinaryField('student_images_NEW', blank=True, null=True)


#@receiver(post_save, sender = 'Student')
#def Student_Signal(sender,instance, created, **kawrgs):
 #   if created:
  #      print(f"A new student '{instance.name}' has been created!")
