# Write your solution here:
	def sort_by_seasons(items: list):
	    # items.sort(key=order_of_sort)# sorts the elements into the parameter itself   
	    # return items
	    return sorted(items,key=order_of_sort)# returns sorted data in a new set of data without changing the original
	 
	def order_of_sort(item: dict):      
	    return item['seasons']
	 
	if __name__ == "__main__":
	    shows = [{"name": "Friends", "rating": 8.9, "seasons": 10}, {"name": "Dexter",
	                                                                 "rating": 8.6, "seasons": 9},  {"name": "Simpsons", "rating": 8.7, "seasons": 32}]
	    # print(sort_by_seasons(shows))
	    # print(shows)
	    print(*[f"{serie['name']} {serie['seasons']} seasons" for serie in sort_by_seasons(shows)], sep="\n")



