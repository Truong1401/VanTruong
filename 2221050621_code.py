students = {}
subjects = []
quantity_of_student = int(input("Số lượng sinh viên: "))
quantity_of_subject = int(input("Số lượng môn học: "))
print(' ')
for i in range(quantity_of_subject):
    subjects.append(input(f'Nhập tên môn học {i + 1}: '))
print(' ')
for i in range(1, quantity_of_student + 1):
    students[i] = {}
    students[i]['name'] = input(f'Tên sinh viên {i}: ')
    students[i]['grade'] = {}
    for j in range(quantity_of_subject):
        students[i]['grade'][subjects[j]] = float(input(f'Nhập điểm môn {subjects[j]}: '))
    print(' ')
for student in students:
    print('________________________')
    print(f'Student ID: {student}')
    print('Name:', students[student]['name'])
    average_grade = 0 
    for grade in range(quantity_of_subject):
        print(subjects[grade], ':', students[student]['grade'][subjects[grade]])
        average_grade += students[student]['grade'][subjects[grade]]
    print('Average grade:', average_grade / quantity_of_subject)     
    print('________________________')
