# Write your solution here:
	class Book:
	    def __init__(self,name,author,genre,year):
	        self.name = name
	        self.author = author
	        self.genre = genre
	        self.year = year
	 
	 
	if __name__=="__main__":
	    metham = Book("The Methamorphosis","Franz Kafka","Science fiction", 1936)
	    thrones = Book("Game of Thrones", "R.R. Martin","Fantasy",2004)
	    
	    print(f"My first read book was {metham.name}, written by {metham.author} in {metham.year}. It's a {metham.genre} story")
	    print()
	    print(f"Name: {thrones.name}")
	    print(f"Author: {thrones.author}")
	    print(f"Genre: {thrones.genre}")
	    print(f"Year: {thrones.year}")
	 
