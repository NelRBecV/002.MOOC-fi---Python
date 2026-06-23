# Write your solution after the class ExamSubmission
	# Do not make changes to the class!
	class ExamSubmission:
	    def __init__(self, examinee: str, points: int):
	        self.examinee = examinee
	        self.points = points
	 
	    def __str__(self):
	        return self.examinee,self.points
	 
	# # WRITE YOUR SOLUTION HERE:
	def passed(submission:list,lowest_passing:int):
	    aproved = []
	    for sub_stdnt in submission:
	        if sub_stdnt.points >= lowest_passing:
	              aproved.append(sub_stdnt)
            
	    return aproved
	 
	if __name__=="__main__":
	    s1 = ExamSubmission("Peter", 12)
	    s2 = ExamSubmission("Pippa", 19)
	    s3 = ExamSubmission("Paul", 15)
	    s4 = ExamSubmission("Phoebe", 9)
	    s5 = ExamSubmission("Persephone", 17)
	 
	    passes = passed([s1, s2, s3, s4, s5], 15)
	    for passing in passes:
	        print(f"ExamSbmission (examinee: {passing.examinee}, points: {passing.points})")
	 



