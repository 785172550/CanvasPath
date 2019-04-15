from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from users.models import CustomUser, Course, Enrolls, Exams, Exam_grades, Homework, Homework_grades

from django.template.defaulttags import register
# Create your views here.

@login_required
def index(request):
    user = request.user
    if user.role == 'S':
        enrolls = Enrolls.objects.filter(student_email=user.email).all()
        courses = [enroll.course_id for enroll in enrolls]
        # exam_info = Exam_grades.objects.filter(course_id__in=courses, student_email=user.email).all()
        grades = Exam_grades.objects.filter(course_id__in=courses, student_email=user.email).all()

        gl = {gra.course_id: gra.grade for gra in grades}
        # for co in courses:
        #     if Exam_grades.objects.filter(course_id__in=courses, student_email=user.email).count() != 0:
        #         co.grade = Exam_grades.objects.filter(course_id__in=courses, student_email=user.email).first().grade
        #     if Homework.objects.filter(course_id=co.)

        return render(request, "index.html", locals())
    elif user.role == 'P':
        print(str(user.get_role_display) + " login success!")
        return render(request, "prof-index.html")
    else:
        students = CustomUser.objects.filter(role='S').all()
        profs = CustomUser.objects.filter(role='P').all()
        courses = Course.objects.all()
        return render(request, "admin.html", locals())


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)