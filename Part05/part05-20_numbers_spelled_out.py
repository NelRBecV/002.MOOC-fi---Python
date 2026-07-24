# Write your solution here
def dict_of_numbers():
	dict_num: dict = {}
	units: list =['zero','one','two','three','four','five','six','seven','eight','nine']
	two_ciphers: list = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	tens: list = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

	for i in range(100):
		if 0 <= i < 10:
			dict_num[i] = units[i]
		elif 10 <= i < 20:
			dict_num[i] = two_ciphers[i-10]
		elif i >= 20:
			if i % 10 == 0:
				p = int(i/10)-2
				dict_num[i] = tens[p]
			else:
				d = int(str(i)[0])
				u = int(str(i)[1])
				dict_num[i] = f"{tens[d-2]}-{units[u]}"

	return dict_num


if __name__ == "__main__":
	dictionary = dict_of_numbers()
	print(dictionary[31])
	print(dictionary[10])
	print(dictionary[90])
