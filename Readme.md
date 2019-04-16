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

查询带字段名的所有记录，就是将所有记录以key-value的形式保存在字典中
Student.objects.all().values()

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

student cvs:

```$xslt
['Full Name', 'Email', 'Age', 'Zip', 'Phone', 'Gender', 'City', 'State', 'Password', 'Street', 'Major', 'Courses 1', 'Course 1 Name', 'Course 1 Details', 'Course 1 Type', 'Course 1 Section', 'Course 1 Section Limit', 'Course 1 HW_No', 'Course 1 HW_Details', 'Course 1 HW_Grade', 'Course 1 EXAM_No', 'Course 1 Exam_Details', 'Course 1 EXAM_Grade', 'Courses 2', 'Course 2 Name', 'Course 2 Details', 'Course 2 Type', 'Course 2 Section', 'Course 2 Section Limit', 'Course 2 HW_No', 'Course 2 HW_Details', 'Course 2 HW_Grade', 'Course 2 EXAM_No', 'Course 2 Exam_Details', 'Course 2 EXAM_Grade', 'Courses 3', 'Course 3 Name', 'Course 3 Details', 'Course 3 Type', 'Course 3 Section', 'Course 3 Section Limit', 'Course 3 HW_No', 'Course 3 HW_Details', 'Course 3 HW_Grade', 'Course 3 EXAM_No', 'Course 3 Exam_Details', 'Course 3 EXAM_Grade']
['Alisa Lynch', 'aly8942@lionstate.edu', '19', '62901', '1507045398', 'F', 'Carbondale', 'Illinois', 'ixg1libp', '78 South Brewery Ave. ', 'CHEM', 'EE320', 'Network Security and Cryptography', 'Regular 3 credit course offered only on campus', 'Reg', '1.0', '40', '1.0', 'Submit this homework on CanvasPath. Grade is out of 100', '93.0', '1.0', 'Closed book exam for 100 marks', '86.0', 'EE212', 'Introduction to Signal Conditioning ', 'Regular 3 credit course offered only on campus', 'Reg', '1.0', '40', '1.0', 'Submit this homework on CanvasPath. Grade is out of 100', '85.0', '1.0', 'Closed book exam for 100 marks', '81.0', 'CMPEN454', 'Fundamentals of Computer Vision', 'Regular 3 credit course offered only on campus', 'Cap', '2.0', '30', '1.0', 'Submit this homework on CanvasPath. Grade is out of 100', '90.0', '', '', '']

email aly8942@lionstate.edu
password ixg1libp
```
