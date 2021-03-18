import pandas as pd
student_dt=pd.read_csv('student.csv')
#print(student_dt)
male_student=student_dt.gender == 'M'
#print(male_student)
data_of_male_students=student_dt[male_student]
#print(data_of_male_students)
male_and_good_student=data_of_male_students.ParentschoolSatisfaction=='Good'
#print(male_and_good_student)
studentgoodmale=data_of_male_students[male_and_good_student]
print(studentgoodmale)
