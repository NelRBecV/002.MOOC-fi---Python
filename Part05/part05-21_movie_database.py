# Write your solution here
	def add_movie(database:list,name:str,director:str,year:int,runtime:int):
	    movie_dict:dict = {'name':name,
                         'director':director,
                         'year':year,
                         'runtime':runtime
                        }
    
	    database.append(movie_dict)
	 
	if __name__=="__main__":
	    data_base:list = []
	    add_movie(data_base, "Black Hawk Down","Riddley Scott",2005,128)
	    add_movie(data_base, "Gone with the Python", "Victor Pything", 2017, 116)
	    add_movie(data_base, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
	    print(data_base)
	 
	 
