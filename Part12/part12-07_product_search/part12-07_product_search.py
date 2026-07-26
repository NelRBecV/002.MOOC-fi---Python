# Write your solution here
	def search(products: list, criterion: callable):
	    result = []   
	    for product in products:
	        if criterion(product):
	            result.append(product)
	    return result
	 
	def cheapest_price(products: list):
	    def price(product:tuple):                 
	        return product[1]        
	    return sorted(products, key=price)
	 
	def most_stock(products:list):
	    return max(products, key=lambda product: product[1])
	 
	if __name__ == "__main__":
	    product_list = [("banana", 5.95, 12),
	                    ("apple", 3.95, 3), 
	                    ("orange", 4.50, 2),
	                    ("watermelon", 4.95, 22),
	                    ("kale", 0.99, 1)]
	 
	    # cheapest = search(product_list,cheapest_price)
	    # print(cheapest)
	 
	  
	 
	    print(search(product_list, lambda price: price[2] % 4 == 0))
	  



