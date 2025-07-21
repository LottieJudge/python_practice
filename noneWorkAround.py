def studentGrades(name, age, grades=None):
    if grades is None:
        grades = []
    return{
        'name': name,
        'age':age,
        'grades':grades
        }

def addGrade(student, grade):
    student['grades'].append(grade)
    print(student['grades'])

lottie = studentGrades('Lottie', 31)
addGrade(lottie, 100)
print(lottie)

# using it mutable instead will result in 

def studentGradesWrong(name, age, grades=[]):
    return{
        'name': name,
        'age':age,
        'grades':grades
        }

def addGradesWrong(student, grade):
    student['grades'].append(grade)
    print(student['grades'])

lottieWrong = studentGradesWrong('Lottie', 31)
addGradesWrong(lottieWrong, 23)

watson = studentGradesWrong('Watson', 8)
addGradesWrong(watson, 23)


# the above print [23] /n [23, 23] - it's remembering each input and giving that back.