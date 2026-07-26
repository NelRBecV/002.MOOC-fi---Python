from functools import reduce
	 
	class CourseAttempt:
	    def __init__(self, course_name: str, grade: int, credits: int):
	        self.course_name = course_name
	        self.grade = grade
	        self.credits = credits
	 
	    def __str__(self):
	        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"
	 
	# Write your solution
	def sum_of_all_credits(courses: list):
	    return reduce(lambda credit, course: credit + course.credits, courses, 0)
	 
	def sum_of_passed_credits(courses:list):
	    return reduce(lambda credit, cre_stdnt: credit + cre_stdnt.credits, list(filter(lambda student: student.grade > 0, courses)), 0)
	 
	def average(courses:list):
	    passed = list(filter(lambda student: student.grade > 0, courses))
	    return reduce(lambda grade, grades: (grade + grades.grade), passed,0) /len(passed)
	    
	 
	if __name__ == "__main__":
	    s1 = CourseAttempt("Introduction to Programming", 5, 5)
	    s2 = CourseAttempt("Advanced Course in Programming", 0, 5)
	    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
	    credit_sum = sum_of_all_credits([s1, s2, s3])
	    print(credit_sum)
	    passed_credits = sum_of_passed_credits([s1, s2, s3])
	    print(passed_credits)
	    average_grade = average([s1, s2, s3])
	    print(average_grade)
	 



