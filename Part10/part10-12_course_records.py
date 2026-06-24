# tee ratkaisusi tänne
	class Course:
	    def __init__(self,name:str):
	        self._name = name
	        self._grade = 0
	        self._credits = 0 
	 
	    def add_course(self, grade:int, credits:int):        
	        self._credits = credits
	        if grade > self._grade:
	            self._grade = grade
	 
	    @property
	    def credits(self):
	        return self._credits
	 
	    @property
	    def grade(self):
	        return self._grade
	 
	    def __str__(self) -> str:
	        return f"{self._name} ({self._credits} cr) grade {self._grade}"
	 
	class InternalProcess:
	    def __init__(self) -> None:
	        self._courses_enrolled = {}
	 
	    def search_for_courses(self,course:str):
	        if not course in self._courses_enrolled:
	            print("no entry for this course")
	            return
            
	        print(self._courses_enrolled[course])
	 
	    def adding_courses(self, course: str):
	        if not course in self._courses_enrolled:
	            self._courses_enrolled[course] = Course(course)
            
	        grade = int(input("grade: "))
	        credits = int(input("credits: "))
	        self._courses_enrolled[course].add_course(grade,credits)
	 
	    def gather_all_courses(self):
	       return self._courses_enrolled
	 
	class UserInterface:
	    def __init__(self):
	        self.database = InternalProcess()
	 
	    def menu(self):
	        print("1 add course")
	        print("2 get course data")
	        print("3 statistics")
	        print("0 exit")
	 
	 
	    def enroll_course(self):
	        course = input("course: ")
	        self.database.adding_courses(course)
	 
	    def show_courses_data(self):       
	        all_courses = self.database.gather_all_courses()
	        credits = 0
	        sum_grades = 0
	        grades = {}
        
	        for course in all_courses.values():
	            credits += course.credits
	            sum_grades += course.grade
	            if course.grade not in grades:
	                grades.update({course.grade:0})
	            grades[course.grade] += 1
            
	        print(f"{len(all_courses)} completed courses, a total of {credits} credits")
	        print(f"mean {round(sum_grades/len(all_courses),1)}")
	        print(f"grade distribution")
        
	        for g in range(5,0,-1):
	            if g not in grades:
	                print(f"{g}:")
	                continue
	            print(f"{g}: {'x'*grades[g]}")
	 
	    def retreive_course_info(self):
	        course = input("course: ")
	        self.database.search_for_courses(course)
	 
	    def run_program(self):
	        self.menu()
	        while True:
	            print()
	            option = input("command: ")
	            if option == "1":
	                self.enroll_course()
	            elif option == "2":
	                self.retreive_course_info()
	            elif option == "3":
	                self.show_courses_data()          
	            elif option == "0":
	                break
	 
	interface = UserInterface()
	interface.run_program()
 
