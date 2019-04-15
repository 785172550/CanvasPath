### CanvasPath 
is a startup project which aims to help Lion State University maintain their software
system for course information management.

* env: 
```
python 3.5
django 2.1.7
numpy 1.14.3
pandas 0.23.1
```

```$xslt

common shell:

from django.contrib.auth.hashers import make_password
user.password = make_password(password)
user.save()

from users.models import *
CustomUser.objects.all()
CustomUser.objects.create(username='student1', email='student1@gmail.com', password='123', role='S', first_name='jack')

Enrolls
Enrolls.objects.create(student_email_id='student1@gmail.com',course_id_id='EE320',section_no_id='1.0')

Course
Department

Sections
Sections.objects.create(sec_no='1.0',section_type='0',course_id='EE320',limit=40)


function assign_prof(course_id, email){
  $.ajax({
  type: 'POST',
  url: url,
  data: data,
  success: success,
  dataType: dataType
});

  $.post(url,data,success(data, textStatus, jqXHR),dataType)
  $.get(URL,callback);
  
}

---------
hw = Homework.objects.filter(course_id,sec_no).all()
hw_grades = Homework_grades.objects.filter(hw_no_in=hw.hw_no,student_email).all()


for gra in hw_grades:
 map[hw_no] = gra.grade

-----------

功能：
UserLogIn:

admin:
1.manage the courses (add/remove),
2.assign professors to courses
3.enroll students to courses and sections

prof:
1.create assignments inside the section he is teaching. The assignments include homeworks and exams
2.SubmitingScores:: should be a grades page for each assignment which includes a table whose columns are the student’s IDs and grades
3.OrganizingTeams: The faculty member should maintain the team list and the members of each team

student: CheckingInfo, course info, hw info, grade info.

```
