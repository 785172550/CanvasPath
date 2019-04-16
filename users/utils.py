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
from users.models import CustomUser, Course, Sections, Homework, Homework_grades, Enrolls
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
    ################### =========================
    if Sections.objects.filter(sec_no2=row[15], section_type=row[14]).count() == 0:
        Sections.objects.create(sec_no2=row[15], section_type=row[14], limit=row[16])
        print("Sections: " + row[15])
    if Sections.objects.filter(sec_no2=row[27], section_type=row[26]).count() == 0:
        Sections.objects.create(sec_no2=row[27], section_type=row[26], limit=row[28])
        print("Sections: " + row[27])
    if Sections.objects.filter(sec_no2=row[39], section_type=row[38]).count() == 0:
        Sections.objects.create(sec_no2=row[39], section_type=row[38], limit=row[40])
        print("Sections: " + row[39])
    ############## ===================================
    # course 1
    # if Course.objects.filter(course_id=row[11]).count() == 0:
    #     Course.objects.create(course_id=row[11], course_name=row[12], course_description=row[13],
    #                           section=Sections.objects.filter(sec_no2=row[15], section_type=row[14]).first(),
    #                           grade=row[22])
    #     print("course: " + row[11])
    # else:
    #     Course.objects.filter(course_id=row[11]).update(course_name=row[12], course_description=row[13],
    #                                                     section=Sections.objects.filter(sec_no2=row[15],
    #                                                                                     section_type=row[14]).first(),
    #                                                     grade=row[22])
    Course.objects.update_or_create(course_id=row[11], course_name=row[12], course_description=row[13],
                                    section=Sections.objects.filter(sec_no2=row[15],
                                                                    section_type=row[14]).first(),
                                    grade=row[22])
    Enrolls.objects.update_or_create(course_id_id=row[11], student_email_id=row[1], section_no=Sections.objects.filter(sec_no2=row[15],
                                                                                                                       section_type=row[14]).first())
    # print(Sections.objects.filter(sec_no2=row[15], section_type=row[14]).first())

    # course 2
    # if Course.objects.filter(course_id=row[23]).count() == 0:
    Course.objects.update_or_create(course_id=row[23], course_name=row[24], course_description=row[25],
                          section=Sections.objects.filter(sec_no2=row[27], section_type=row[26]).first(),
                          grade=row[34])
        # print(Sections.objects.filter(sec_no2=row[27], section_type=row[26]).first())
    print("course: " + row[23])
    # else:
    #     Course.objects.filter(course_id=row[23]).update(course_name=row[24], course_description=row[25],
    #                                                     section=Sections.objects.filter(sec_no2=row[27],
    #                                                                                     section_type=row[26]).first(),
    #                                                     grade=row[34])
    Enrolls.objects.update_or_create(course_id_id=row[23], student_email_id=row[1], section_no=Sections.objects.filter(sec_no2=row[27], section_type=row[26]).first())
    # course 3
    # if Course.objects.filter(course_id=row[35]).count() == 0:
    Course.objects.update_or_create(course_id=row[35], course_name=row[36], course_description=row[37],
                          section=Sections.objects.filter(sec_no2=row[39], section_type=row[38]).first(),
                          grade=row[46])
        # print(Sections.objects.filter(sec_no2=row[39], section_type=row[38]).first())
    print("course: " + row[35])
    # else:
    #     Course.objects.filter(course_id=row[35]).update(course_id=row[35], course_name=row[36],
    #                                                     course_description=row[37],
    #                                                     section=Sections.objects.filter(sec_no2=row[39],
    #                                                                                     section_type=row[38]).first(),
    #                                                     grade=row[46])
    Enrolls.objects.update_or_create(course_id_id=row[35], student_email_id=row[1], section_no=Sections.objects.filter(sec_no2=row[39], section_type=row[38]).first())
    #####===============================================
    # hw 1
    if Homework_grades.objects.filter(course_id=row[11], student_email=row[1]).count() == 0:
        Homework_grades.objects.create(course_id_id=row[11], student_email_id=row[1], hw_details=row[18],
                                       grade=row[19])
        print("Homework_grades: " + row[11])
    else:
        Homework_grades.objects.filter(course_id=row[11], student_email=row[1]).update(hw_details=row[18],
                                                                                       grade=row[19])
        # print(Sections.objects.filter(sec_no2=row[15], section_type=row[14]).first())

    # hw 2
    if Homework_grades.objects.filter(course_id=row[23], student_email=row[1]).count() == 0:
        Homework_grades.objects.create(course_id_id=row[23], student_email_id=row[1], hw_details=row[30],
                                       grade=row[31])
        # print(Sections.objects.filter(sec_no2=row[27], section_type=row[26]).first())
        print("Homework_grades: " + row[23])
    else:
        Homework_grades.objects.filter(course_id=row[23], student_email=row[1]).update(hw_details=row[30],
                                                                                       grade=row[31])
    # hw 3
    if Homework_grades.objects.filter(course_id=row[35], student_email=row[1]).count() == 0:
        Homework_grades.objects.create(course_id_id=row[35], student_email_id=row[1], hw_details=row[42],
                                       grade=row[43])
        # print(Sections.objects.filter(sec_no2=row[39], section_type=row[38]).first())
        print("Homework_grades: " + row[35])
    else:
        Homework_grades.objects.filter(course_id=row[35], student_email=row[1]).update(hw_details=row[42],
                                                                                       grade=row[43])

print(rows[0])
# print(rows[1])
# print(rows[1:3])

# row[14] course1 type, row15 sectio no, row16 limit, row26 c2 type, row27 sec no, c28 limit, row38 type, row39 sec, row40 limit
# Street row9,
