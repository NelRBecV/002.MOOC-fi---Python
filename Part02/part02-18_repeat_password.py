# Write your solution here
password = input("Password:")
repeat_pwd = ""
while password != repeat_pwd:
	repeat_pwd = input("Repeat password:")
	if password != repeat_pwd:
		print("They do not match!")
print("User account created!")
