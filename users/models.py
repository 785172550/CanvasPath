from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.

class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    type_choices = (
        ('SU', 'Super User'),
        ('S', 'Student'),
        ('P', 'Professor'),
    )
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=1, null=True)
    role = models.CharField(max_length=2, choices=type_choices, default='S')

    # student
    major = models.TextField(null=True)
    street = models.TextField(null=True)
    zipcode = models.TextField(null=True)

    # professor
    office_address = models.TextField(null=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)  # many to one
    title = models.TextField(null=True)


# Professor (email, password, name, age, gender, office_address, department, title)
# class Professor(AbstractUser):
#     objects = CustomUserManager()
#     age = models.IntegerField(null=True)
#     gender = models.BooleanField(null=True)
#     office_address = models.TextField(null=True)
#     department = models.ForeignKey('Department', on_delete=models.DO_NOTHING)
#     title = models.TextField(null=True)



class Department(models.Model):  # Department (dept_id, dept_name, dept_head)
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.TextField(null=True)
    dept_head = models.TextField(null=True)


# Course (course_id, course_name, course_description)
class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=10)
    course_name = models.TextField()
    course_description = models.TextField(null=True)
    course_prof = models.ForeignKey('CustomUser', to_field='email', on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey('Sections', on_delete=models.SET_NULL, null=True)
    grade = models.CharField(max_length=5, null=True)


# Sections (course_id, sec_no, section_type, limit, teaching_team_id) “section_type” is regular/capstone
#  “limit” is the maximum enrollments allowed
class Sections(models.Model):
    sec_no = models.AutoField(primary_key=True)
    sec_no2 = models.CharField(max_length=10, null=True)
    section_type = models.CharField(max_length=10, choices=[(0, 'regular'), (1, 'capstone')])
    # course_id = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    limit = models.IntegerField(default=10)


# Enrolls (student_email, course_id, section_no)
class Enrolls(models.Model):
    student_email = models.ForeignKey('CustomUser', to_field='email', on_delete=models.CASCADE)
    course_id = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    section_no = models.ForeignKey('Sections', on_delete=models.SET_NULL, null=True)


# teaching_team_id
class Prof_teams(models.Model):
    teaching_team_id = models.IntegerField(primary_key=True)


# Prof_team_members (prof_email, teaching_team_id)
class Prof_team_members(models.Model):
    prof_email = models.ForeignKey('CustomUser', to_field='email',
                                   on_delete=models.SET_NULL, null=True)
    teaching_team_id = models.IntegerField(default=0)


# Homework (course_id, sec_no, hw_no, hw_details)
# - “hw_no” is an integer. Sections have homeworks from 1 – n
# - “hw_details” is a short description of the homework
class Homework(models.Model):
    hw_no = models.IntegerField(primary_key=True)
    hw_details = models.TextField(null=True)
    course_id = models.ForeignKey('Course', to_field='course_id', on_delete=models.SET_NULL, null=True)
    sec_no = models.ForeignKey('Sections', to_field='sec_no', on_delete=models.SET_NULL, null=True)


# Homework_grades (student_email, course_id, sec_no, hw_no, grade)
class Homework_grades(models.Model):
    hw_no = models.ForeignKey('Homework', to_field='hw_no', on_delete=models.SET_NULL, null=True)
    student_email = models.ForeignKey('CustomUser', to_field='email', on_delete=models.SET_NULL, null=True)
    grade = models.CharField(max_length=5)

    class Meta:
        unique_together = ("hw_no", "student_email")


# Exams (course_id, sec_no, exam_no, exam_details)
class Exams(models.Model):
    exam_no = models.IntegerField(primary_key=True)
    exam_details = models.TextField(null=True)
    course_id = models.ForeignKey('Course', to_field='course_id', on_delete=models.SET_NULL, null=True)
    sec_no = models.ForeignKey('Sections', to_field='sec_no', on_delete=models.SET_NULL, null=True)


# Exam_grades (student_email, course_id, sec_no, exam_no, grades)
# “exam_no” is an integer. Sections have exams from 1 – n
# - “exam_details” is a short description of the exam
class Exam_grades(models.Model):
    exam_no = models.ForeignKey('Exams', to_field='exam_no', on_delete=models.SET_NULL, null=True)
    student_email = models.ForeignKey('CustomUser', to_field='email', on_delete=models.SET_NULL, null=True)
    course_id = models.ForeignKey('Course', to_field='course_id', on_delete=models.SET_NULL, null=True)
    grade = models.CharField(max_length=5)

    class Meta:
        unique_together = ("exam_no", "student_email", "course_id")


class Capstone_section(models.Model):  # Capstone_section (course_id, sec_no, project_no, sponsor_id)
    sec_no = models.IntegerField(primary_key=True)
    course_id = models.OneToOneField('Course', on_delete=models.SET_NULL, null=True)
    project_no = models.TextField(null=True)
    sponsor_id = models.ForeignKey('CustomUser', to_field='email', on_delete=models.SET_NULL, null=True)


class Capstone_Team(models.Model):  # Capstone_Team (course_id, sec_no, capstone_team_id, project_no)
    capstone_team_id = models.IntegerField(primary_key=True)
    sec_no = models.ForeignKey('Capstone_section', on_delete=models.SET_NULL,
                               null=True)
    course_id = models.OneToOneField('Course', on_delete=models.SET_NULL, null=True)
    project_no = models.TextField(null=True)


# no primary key
class Capstone_Team_Members(models.Model):  # Capstone_Team_Members(student_email, capstone_team_id, course_id, sec_no)
    capstone_team_id = models.ForeignKey('Capstone_Team', on_delete=models.SET_NULL, null=True)
    student_email = models.ForeignKey('CustomUser', to_field='email', on_delete=models.SET_NULL, null=True)
    sec_no = models.ForeignKey('Capstone_section', on_delete=models.SET_NULL,
                               null=True)
    course_id = models.OneToOneField('Course', on_delete=models.SET_NULL, null=True)


class Capstone_grades(models.Model):  # Capstone_grades(course_id, sec_no, capstone_team_id, grade)
    sec_no = models.ForeignKey('Capstone_section', on_delete=models.SET_NULL, null=True)
    course_id = models.OneToOneField('Course', on_delete=models.SET_NULL, null=True)
    team_id = models.OneToOneField('Capstone_Team', on_delete=models.SET_NULL, null=True)
    grade = models.IntegerField(default=0)

    class Meta:
        unique_together = ("sec_no", "team_id")
