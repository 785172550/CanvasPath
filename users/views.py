from django.shortcuts import render, redirect
from .forms import LoginForm, CourseForm, UserForm
from django.contrib.auth import login as slogin, authenticate, logout as slogout
from .models import CustomUser, Course, Enrolls, Sections
from django.http import JsonResponse, HttpResponse


# Create your views here.
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        message = "please check forms！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                slogin(request, user)
                print(user.username + " login success!")
                return redirect('/index')
            else:
                message = "loging error"
                return render(request, 'login.html', locals())
        return render(request, 'login.html', locals())
    else:
        login_form = LoginForm()
        return render(request, 'login.html', locals())


def logout(request):
    slogout(request)
    return redirect('login')


def manage_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_id = course_form.cleaned_data['course_id']
            name = course_form.cleaned_data['course_name']
            description = course_form.cleaned_data['course_description']
            course = Course.objects.get(course_id=course_id)
            if course:
                course.course_description = description
                course.save()
            else:
                Course.objects.create(course_id=course_id, course_name=name, course_description=description)
    elif request.method == 'GET':
        course_id = request.GET.get('delete_id', None)
        if course_id:
            Course.objects.get(course_id=course_id).delete()
    redirect('index')


def manage_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            password = course_form.cleaned_data['password']
            role = course_form.cleaned_data['role']
            name = course_form.cleaned_data['name']
            u = CustomUser.objects.get(username=username)
            if u:
                CustomUser.objects.filter(username=username).update(email=email, password=password, role=role,
                                                                    first_name=name)
            else:
                CustomUser.objects.create(username=username, email=email, password=password, role=role, first_name=name)


def enroll_student(request):
    if request.method == 'GET':
        email = request.GET.get('student_email', None)
        course_id = request.GET.get('course', None)
        sec_no = Sections.objects.filter(course_id=course_id).all()
        en = Enrolls.objects.create(student_email=email, course_id=course_id, section_no=sec_no)
        return JsonResponse(en)


def assign_prof(request):
    if request.method == 'GET':
        email = request.GET.get('prof_email', None)
        course_id = request.GET.get('course', None)
        # sec_no = Sections.objects.filter(course_id=course_id).all()
        cour = Course.objects.filter(course_id=course_id).update(course_prof=email)
        return JsonResponse(cour)


def create_hw(request):
    pass


def create_exam(request):
    pass


def create_hw_grade(request):
    pass


def create_exam_grade(request):
    pass
