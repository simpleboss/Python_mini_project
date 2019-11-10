subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
subjects.append("computer science")
grades.append(100)
gradebook = list(zip(subjects, grades))
gradebook.append(["visual arts", 93])
#print(gradebook)

last_semester_grade = [50, 60, 70, 80, 90]
last_semester_gradebook = list(zip(subjects, last_semester_grade))

full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)