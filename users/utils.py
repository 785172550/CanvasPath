# coding:utf-8
# life is short, you need Python！

# import pandas as pd
# import numpy as np
# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)
# df = pd.read_csv('../static/1_Students.csv', header=None,
#                  sep=',')
# print(df.head(10))

import os
import django

os.environ.setdefault('DJANGO_SETTING_MODULE', 'canvas_path.settings')

django.setup()
import csv
from users.models import CustomUser, Course, Sections
from django.contrib.auth.hashers import make_password

with open('../static/1_Students.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]

for row in rows[1:10]:
    if CustomUser.objects.filter(email=row[1]).count() == 0:
        CustomUser.objects.create(first_name=row[0], username=row[1], email=row[1], role='S', age=row[2],
                                  zipcode=row[3], gender=row[5], password=make_password(row[8]), street=row[9])
        print("user: " + row[1])
    else:
        CustomUser.objects.filter(email=row[1]).update(first_name=row[0], username=row[1], role='S', age=row[2],
                                                       zipcode=row[3], gender=row[5], password=make_password(row[8]),
                                                       street=row[9])

    if Sections.objects.filter(sec_no2=row[15], section_type=row[14]).count() == 0:
        Sections.objects.create(sec_no2=row[15], section_type=row[14], limit=row[16])
        print("Sections: " + row[15])

    if Sections.objects.filter(sec_no2=row[27], section_type=row[26]).count() == 0:
        Sections.objects.create(sec_no2=row[27], section_type=row[26], limit=row[28])
        print("Sections: " + row[27])

    if Sections.objects.filter(sec_no2=row[39], section_type=row[38]).count() == 0:
        Sections.objects.create(sec_no2=row[39], section_type=row[38], limit=row[40])
        print("Sections: " + row[39])

    if Course.objects.filter(course_id=row[11]).count() == 0:
        Course.objects.create(course_id=row[11], course_name=row[12], course_description=row[13],
                              section=Sections.objects.filter(sec_no2=row[15], section_type=row[14]).first())
        print(Sections.objects.filter(sec_no2=row[15], section_type=row[14]).first())
        print("course: " + row[11])

print(rows[0])
# print(rows[1])
# print(rows[1:3])

# row[14] course1 type, row15 sectio no, row16 limit, row26 c2 type, row27 sec no, c28 limit, row38 type, row39 sec, row40 limit
# Street row9,