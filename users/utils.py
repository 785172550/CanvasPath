# coding:utf-8
# life is short, you need Python！
# import pandas as pd
# import numpy as np
# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)
# reader = pd.read_csv('../static/1_Students.csv', header=None,
#                  sep=',')
#
# rows= [row[1] for row in reader]
#
# print(rows)
# print(df.head())

import os
import django

os.environ.setdefault('DJANGO_SETTING_MODULE', 'canvas_path.settings')

django.setup()
import csv
from users.models import CustomUser, Course
from django.contrib.auth.hashers import make_password

with open('../static/1_Students.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]

# print(CustomUser.objects.filter(email='test'))
for row in rows[1:10]:
    if CustomUser.objects.filter(email=row[1]).count() == 0:
        CustomUser.objects.create(first_name=row[0], username=row[1], email=row[1], role='S', age=row[2],
                                  zipcode=row[3], gender=row[5], password=make_password(row[8]), street=row[9])
        print("user: " + row[1])
    else:
        CustomUser.objects.filter(email=row[1]).update(first_name=row[0], username=row[1], role='S', age=row[2],
                                                    zipcode=row[3], gender=row[5], password=make_password(row[8]),
                                                    street=row[9])

    if Course.objects.filter(course_id=row[11]).count() == 0:
        Course.objects.create(course_id=row[11], course_name=row[12], course_description=row[13])
        print("course: " + row[11])

# print(rows[0])
# print(rows[1])
# print(rows[1:3])
