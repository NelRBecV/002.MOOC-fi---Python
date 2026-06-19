# Write your solution here
import math


def get_station_data(filename:str):
    stations: dict = {}
    with open(filename) as data:
        for record in data:
            station = record.split(";")
            if station[0] == "Longitude":
                continue
            
            stations.update({station[3]:(float(station[0]),float(station[1]))})
          
    return stations
	 
def distance(stations:dict, station1:str,station2:str):
	    
	long_a: float = 0
	lat_a: float = 0
	long_b: float = 0
	lat_b: float = 0
  
	if station1 in stations:
		long_a,lat_a = stations[station1]
	if station2 in stations:
		long_b,lat_b = stations[station2]
	
	x_km = (long_a - long_b) * 55.26
	y_km = (lat_a - lat_b) * 111.2
	distance_km = math.sqrt(x_km**2 + y_km**2)
 
	return distance_km
 
def greatest_distance(stations: dict):
	greatest:float=0
	city_1: str = ""
	city_2: str = ""

	for city_a in stations.keys():
		for city_b in stations.keys():            
			if city == city2:
				continue
			
			city_distance = distance(stations, city_a,city_b)            
			if city_distance > greatest:
				greatest = city_distance
				city_1=city_a
				city_2=city_b
			
	return city_1,city_2,greatest
	 
	if __name__=="__main__":
	    
	    file_search =  input("Stations file: ")    
	    my_stations = get_station_data(file_search)
	    cal_distance = distance(my_stations,"Designmuseo","Hietalahdentori")
	    print(cal_distance)
	    cal_distance = distance(my_stations,"Viiskulma","Kaivopuisto")
	    print(cal_distance)
	    
	    station1, station2, greatest = greatest_distance(my_stations)
	    print(station1, station2, greatest)
