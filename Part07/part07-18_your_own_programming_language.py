# Write your solution here
	from string import ascii_uppercase


	def run(program:list):
	    variables = {i:0 for i in ascii_uppercase}
	    results:list = []
	    n = 0
    
	    while n < len(program) and program[n] != "END":
	        commands = program[n].split(" ")        
	        if commands[0] == "PRINT":# stores numerical values in 'results' list variable to be returned
	            value = variables[commands[1]] if commands[1] in ascii_uppercase else int(commands[1])
	            results.append(value)
            
	        elif commands[0] == "MOV":# changes the value of an element with a new one or copy it from another
	            variables[commands[1]] = int(commands[2]) if not commands[2] in ascii_uppercase else variables[commands[2]]
            
	        elif commands[0] == "ADD":# adds the value of A in B
	            variables[commands[1]] += variables[commands[2]] if commands[2] in variables.keys() else int(commands[2])
            
	        elif commands[0] == "SUB":# substracts the value of B in A
	            variables[commands[1]] -= variables[commands[2]] if commands[2] in variables.keys() else int(commands[2])
            
	        elif commands[0] == "MUL":# multiplies A times in B
	            variables[commands[1]] *= variables[commands[2]] if commands[2] in variables.keys() else int(commands[2])
            
	        elif commands[0] == "JUMP":# searches a keyword in the command list and set the n value with the index of searched word
	            try:
					n = program.index(f"{commands[1]}:")-1				
				except ValueError:
					# if the keyword doesn't exist, the program will end
					n = len(program)
            
	        elif commands[0] == "IF":#makes decisions between A compares to B
	            side_a = variables[commands[1]] if commands[1] in ascii_uppercase else commands[1]
	            side_b = variables[commands[3]] if commands[3] in ascii_uppercase else commands[3]
	            
              if eval(f"{side_a} {commands[2]} {side_b}") == True:
				 try:
		             n = program.index(f"{commands[5]}:")-1
				 except ValueError:
					 n = len(program)

	        n += 1        
	    return results
	        
	if __name__=="__main__":
	    program4 = []
	    program4.append("MOV N 50")
	    program4.append("PRINT 2")
	    program4.append("MOV A 3")
	    program4.append("begin:")
	    program4.append("MOV B 2")
	    program4.append("MOV Z 0")
	    program4.append("test:")
	    program4.append("MOV C B")
	    program4.append("new:")
	    program4.append("IF C == A JUMP error")
	    program4.append("IF C > A JUMP over")
	    program4.append("ADD C B")
	    program4.append("JUMP new")
	    program4.append("error:")
	    program4.append("MOV Z 1")
	    program4.append("JUMP over2")
	    program4.append("over:")
	    program4.append("ADD B 1")
	    program4.append("IF B < A JUMP test")
	    program4.append("over2:")
	    program4.append("IF Z == 1 JUMP over3")
	    program4.append("PRINT A")
	    program4.append("over3:")
	    program4.append("ADD A 1")
	    program4.append("IF A <= N JUMP begin")
	    result = run(program4)
	    print(result)

