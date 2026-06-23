# WRITE YOUR SOLUTION HERE:
	class WeatherStation:
	    def __init__(self, city):
	        self.__city = city
	        self.__obsertvations = []
	    
	    def __str__(self):
	        return f"{self.__city}, {self.number_of_observations()} observations"
	    	    
	    def add_observation(self, data):
	        self.__obsertvations.append(data)
	 
	    
	    def latest_observation(self):
	        if len(self.__obsertvations) != 0:
	            return self.__obsertvations[-1]            
	        return "none"
	 
	    
	    def number_of_observations(self):
	        return len(self.__obsertvations)
	 
	if __name__ == "__main__":
	    station = WeatherStation("Houston")
	    # station.add_observation("Rain 10mm")
	    # station.add_observation("Sunny")
	    print(station.latest_observation())
	 
	    # station.add_observation("Thunderstorm")
	    print(station.latest_observation())
	 
	    print(station.number_of_observations())    
	    print(station)
	    print()
	 



