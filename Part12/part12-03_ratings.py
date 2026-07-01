# TEE RATKAISUSI TÄHÄN:
	def sort_by_ratings(items: list):
	    def by_rating(serie: dict):
	        return serie['rating']
	 
	    return sorted(items,key=by_rating, reverse=True)
	 
	if __name__ == "__main__":
	    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]
	 
	    print("Rating according to IMDB")
	    for serie in sort_by_ratings(shows):
	        print(f"{serie['name']} {serie['rating']}")

