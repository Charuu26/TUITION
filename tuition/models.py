from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from autoslug import AutoSlugField


# Create your models here.

class AttedenceFaculty(models.Model):
    fac_att_id = models.AutoField(primary_key=True)
    f = models.ForeignKey('Faculty',on_delete=models.CASCADE, default="1")
    att_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'attedence_faculty'


class AttedenceStudent(models.Model):
    stu_att_id = models.AutoField(primary_key=True)
    tt = models.ForeignKey('Timetable', on_delete=models.CASCADE, default="1")
    att_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'attedence_student'
        
        

class Faculty(models.Model):
    f_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    con_no = models.CharField(max_length=10, blank=True, null=True)
    joining_date = models.DateField()

    class Meta:
        db_table = 'faculty'


class Standard(models.Model):
    sta_id = models.AutoField(primary_key=True)
    sta_name = models.CharField(unique=True, max_length=30, blank=True, null=True)
    sta_code = models.CharField(max_length=10)
    image1 = models.ImageField(upload_to="standard/", max_length=250, null=True, default=None)
    # image1_slug =AutoSlugField(populate_from='standard_icon',unique=True,null=True,default=None)

    class Meta:
        db_table = 'standard'
        
class Stastudent(models.Model):
    stastu_id = models.AutoField(primary_key=True)
    sta = models.ForeignKey('Standard',on_delete=models.CASCADE,default = "Standard")
    s = models.ForeignKey('Student', on_delete=models.CASCADE,default="Student")
    class Meta:
        db_table = 'stastudent'


class Stasubject(models.Model):
    stasubj_id = models.AutoField(primary_key=True)
    sta = models.ForeignKey('Standard', on_delete=models.CASCADE, related_name='stasubjects')  # Primary reference
    sub = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='stasubjects')  # Subject reference

    class Meta:
        db_table = 'stasubject'



class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=70, blank=True, null=True)
    password = models.CharField(max_length=8, blank=True, null=True)
    con_no = models.CharField(max_length=10, blank=True, null=True)
    username = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'student'


class Subject(models.Model):
    sub_id = models.AutoField(primary_key=True)
    sub_name = models.CharField(unique=True, max_length=100, blank=True, null=True)
    sub_code = models.CharField(max_length=10)

    class Meta:
        db_table = 'subject'

    def __str__(self):
        return self.sub_name


class Timetable(models.Model):
    tt_id = models.AutoField(primary_key=True)
    sta = models.ForeignKey('Standard',on_delete=models.CASCADE,default="Standard")
    f = models.ForeignKey('Faculty', on_delete=models.CASCADE,default="Faculty")
    sub = models.ForeignKey('Subject', on_delete=models.CASCADE,default="Subject")
    day_of_week = models.CharField(max_length=9)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = 'timetable'
        
class admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    
    class Meta:
        db_table = 'admin'
    
        
# class StudentManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
#         student = self.model(username=username, **extra_fields)
#         student.set_password(password)
#         student.save(using=self._db)
#         return student

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(username, password, **extra_fields)

# class Student1(AbstractBaseUser):
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField()
#     address = models.CharField(max_length=255, blank=True, null=True)
#     con_no = models.CharField(max_length=10, blank=True, null=True)
    
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
    
#     objects = StudentManager()

#     def __str__(self):
#         return self.username

from django.db import models

# Create your models here.
