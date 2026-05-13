def get_top_student(students):
    top = students[0]
    for student in students:
        if student[1] > top[1]:
            top = student
    return top[0]
print(get_top_student([('Ali',90),('Sara',95),('Tom',80)]))