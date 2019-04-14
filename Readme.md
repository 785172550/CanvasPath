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


```