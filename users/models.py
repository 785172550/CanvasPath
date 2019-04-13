from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.

class CustomUserManager(UserManager):
    pass


# class Student(AbstractUser):
#     objects = CustomUserManager()
#     email = models.EmailField(_('email address'), blank=True)
#     age = models.IntegerField(null=True)
#     gender = models.BooleanField(null=True)
#     major = models.TextField(null=True)
#     street = models.TextField(null=True)
#     zipcode = models.TextField(null=True)


# Professor (email, password, name, age, gender, office_address, department, title)
# class Professor(AbstractUser):
#     objects = CustomUserManager()
#     age = models.IntegerField(null=True)
#     gender = models.BooleanField(null=True)
#     office_address = models.TextField(null=True)
#     department = models.ForeignKey('Department', on_delete=models.DO_NOTHING)
#     title = models.TextField(null=True)


# Department (dept_id, dept_name, dept_head)
class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.TextField()
    dept_head = models.TextField()


# Course (course_id, course_name, course_description)
class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.TextField()
    course_description = models.TextField()


# Sections (course_id, sec_no, section_type, limit, teaching_team_id) “section_type” is regular/capstone
#  “limit” is the maximum enrollments allowed
class Sections(models.Model):
    pass


class Enrolls(models.Model):
    pass


class Prof_teams(models.Model):
    pass


class Prof_team_members(models.Model):
    pass


class Homework(models.Model):
    pass


class Homework_grades(models.Model):
    pass


class Exams(models.Model):
    pass
