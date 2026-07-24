# Write your solution here
'''
NOTE: intputs must be a string numbers pair at the same line and then press ENTER

Example: 
Exam points and exercises completed: 15 90
Exam points and exercises completed: 12 75
...

This algorythm is written to take the first two values only.
If you type more than two values in the same line, the remaining 
data will loss and the output will not be as expected

"Exam points" goes from 0 to 20
"Completed excercises" takes values by percentage (0 - 100)
'''


def analyze(grades: list):
    data_analyzed: list = []
    total_grades: int = 0
    for g in grades:
        ex = exercise_points(int(g[1]))
        if int(g[0]) >= 10:
            f_grade = get_student_grade(exam=int(g[0]), exer=ex)
        else:
            f_grade = 0
        data_analyzed.append(f_grade)
        total_grades += int(g[0]) + ex
    return data_analyzed, total_grades,


def exercise_points(exercises: int):
    return exercises // 10


def get_student_grade(exam: int, exer: int):
    total_points = exam + exer
    scales: list = [[0, 0, 14], [1, 15, 17], [2, 18, 20], [3, 21, 23], [4, 24, 27], [5, 28, 30]]
    grade = 0
    for p in scales:
        if p[1] <= total_points <= p[2]:
            grade = p[0]
            break
    return grade


def insert_students():
    data: list = []
    while True:
        new_data = input("Exam points and exercises completed: ")
        if new_data != "":
            entry = new_data.split(" ")
            data.append(entry)
        else:
            return data


def show_statistics(info: tuple):
    aproved: int = 0
    grades = [0] * 6
    for i in info[0]:
        grades[i] += 1
        if i > 0:
            aproved += 1

    print("\nStatistics: ")
    print(f"Points average: {info[1] / len(info[0]):.1f}")
    print(f"Pass percentage: {(aproved * 100) / len(info[0]):.1f}")
    print("Grade distribution:")
    for g in range(len(grades) - 1, -1, -1):
        print(f"{g}: {'*' * grades[g]}")


def main():
    students = insert_students()
    analyse_result = analyze(students)
    show_statistics(analyse_result)


main()
