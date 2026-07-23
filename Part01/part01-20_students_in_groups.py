# Write your solution here
students = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))
if students % group_size == 0:
	num_group = (students // group_size)
else:
	num_group = (students // group_size) +1

print(f"Number of groups formed: {num_group}")
