department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456

line1 = 'Department1 name:%-10sManager:%-10s COURSE FEES:%-10.2f The End!' % (department1,depart1_m,COURSE_FEES_SEC)
line2 = 'Department2 name:%-10sManager:%-10s COURSE FEES:%-10.2F The End!' % (department2,depart2_m,COURSE_FEES_Python)
line3 = 'Department1 name:{:<10}Manager:{:10s} COURSE FEES:{:<10.2F} The End!'.format(department1,depart1_m,COURSE_FEES_SEC)
line4 = "Department2 name:{:<10}Manager:{:<10} COURSE FEES:{:<10.2F} The End!".format(department2,depart2_m,COURSE_FEES_Python)

length = len(line1)
print("="*length)
print(line1)
print(line2)
print('='*length)

length3 = len(line3)
print("="*length3)
print(line3)
print(line4)
print('='*length3)


