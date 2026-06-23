# Write your solution here:
	class Series:
	    def __init__(self,name: str, seasons: int, categories: list):
	        self.title = name
	        self.seasons = seasons
	        self.categories = categories
	        self.ratings = []
	        
	    def __str__(self) -> str:
	        average: float = 0.0
          rating: str = ""

	        if len(self.ratings) == 0:
	            rating = "no ratings"
	        else:
	            average = sum(self.ratings)/len(self.ratings)
	            rating = f"{len(self.ratings)} ratings, average {average:.1f} points"            
	           
	        return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.categories)}\n{rating}"
	 
	    def rate(self,rating:int):
	        self.ratings.append(rating)
	    
	def minimum_grade(rating:float, series_list:list):
	    listed_series:list = []
    
	    for serie in series_list:            
	        if sum(serie.ratings)/len(serie.ratings) >= rating:
	            listed_series.append(serie)
            
	    return listed_series
	 
	def includes_genre(genre:str, series_list:list):
	    listed_serie:list = []
	    for serie in series_list:
	        if genre in serie.categories:
	            listed_serie.append(serie)
            
	    return listed_serie
	 
	if __name__ == "__main__":
	    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
	    s1.rate(5)
	 
	    s2 = Series("South Park", 24, ["Animation", "Comedy"])
	    s2.rate(3)
	 
	    s3 = Series("Friends", 10, ["Romance", "Comedy"])
	    s3.rate(2)
	 
	    series = [s1,s2,s3]
    
	    print("Series with a least a rating of 4.5:")    
	    for serie in minimum_grade(4.5,series):
	        print(serie.title)
        
	    print("Series with genre of Comedy:")    
	    for serie in includes_genre("Comedy",series):
	        print(serie.title)

