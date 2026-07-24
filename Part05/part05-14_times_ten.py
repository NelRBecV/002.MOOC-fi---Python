def times_ten(start_index:int,end_index:int):
	ten_times = {}

	while start_index <= end_index:
		ten_times[start_index] = start_index * 10
		start_index +=1

	return ten_times


if __name__ == "__main__":
	print(times_ten(1, 4))
