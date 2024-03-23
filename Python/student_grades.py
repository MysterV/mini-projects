student_scores = {
    "Matt": 90,
    "Harry": 83,
    "John": 53,
    "Ron": 78,
    "Mary": 0,
    "Aubrey": 67,
    "Hero": 100,
    "Basil": 89,
    "Kel": 40
}

student_grades = {}

grades = {
    6: range(96, 101),
    5: range(86, 96),
    4: range(70, 86),
    3: range(55, 70),
    2: range(40, 55),
    1: range(0, 40)
}

for student in student_scores:
    for grade in grades:
        if student_scores[student] in grades[grade]:
            student_grades[student] = grade
            break

print(student_grades)