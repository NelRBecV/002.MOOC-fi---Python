# Write your solution here
import json


class Data:
    def __init__(self) -> None:
        self._file = []
        
    def load_data(self, file: str):
        try:
            with open(file, "r") as data:
                record = json.load(data)
        except FileNotFoundError:
            print(f"File {file} wasn't found")
        else:
            for field in record:                
                self._file.append(field)
 
        return self._file
 
class UserInterface():
    def __init__(self) -> None:
        file = Data()         
        self.__data = file.load_data(input("file name: "))       
 
    def check_for_data(self):
        if len(self.__data) != 0:
            print(f"read the data of {len(self.__data)} players") 
            return True        
        return False
 
    @property
    def data(self):
        return self.__data
 
    def menu(self):
        print()
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
 
    def search_player(self, search: str, pattern: str):        
        return list(filter(lambda player: player[search] == pattern, self.data))
 
    def show_data(self, data: list, dict_index: str):        
            print(
            f"{data['name']:21}{data[dict_index]:>2}{data['goals']:>4} + {data['assists']:>2} = {data['goals']+ data['assists']:>3}")
                   
    def list_team(self):        
         for team in sorted(list(set(map(lambda team: team['team'], self.data)))):
            print(team)
 
    def list_countries(self):
        countries = sorted(list(set(map(lambda country: country['nationality'], self.data))))
        for c in countries:
            print(c)
    
    def interact(self):
        while True:
            print()
            option = input('command: ')            
            if option == "0":
                break
 
            elif option == "1":
                pl_name = input("name: ")
                if len(pl_name) != 0:
                    pl_data = self.search_player("name",pl_name)
                    for data in pl_data:
                        self.show_data(data,"team")
 
            elif option == "2":
                self.list_team()
 
            elif option == "3":
                self.list_countries()
 
            elif option == "4":
                d_index = "team"
                t_name = input("team: ")
                pl_data = self.search_player(d_index, t_name)
                if pl_data != None:
                    team_data = sorted(pl_data,key=lambda player: player['goals'] + player['assists'],reverse=True)
                    for data in team_data:
                        self.show_data(data,d_index)
                    
            elif option == "5":
                d_index = "nationality"
                c_player = input("country: ")
                pl_data = self.search_player(d_index, c_player)
                if pl_data != None:
                    country_data = sorted(
                        pl_data, key=lambda player: player['goals'] + player['assists'], reverse=True)
                    for player in country_data:
                        self.show_data(player ,"team")
 
            elif option == "6":
                times = int(input("how many: "))
                players = sorted(self.data, key=lambda points: points['goals'], reverse=True)
                players.sort(key=lambda points: points['goals'] + points['assists'], reverse=True)
                for t in range(times):                    
                    self.show_data(players[t],"team")
 
            elif option == "7":
                times = int(input("how many: "))
                players = sorted(self.data, key=lambda points: points['games'],)
                players.sort(key=lambda points: points['goals'], reverse=True)
                for t in range(times):
                    self.show_data(players[t],"team")                    
            else:
                print("command not found!")
 
    def execute(self):
        if self.check_for_data():
            self.menu()
            self.interact()
 
 
program = UserInterface()
program.execute()
