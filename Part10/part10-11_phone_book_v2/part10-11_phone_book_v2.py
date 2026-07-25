# Write your solution here:
class Person:
    def __init__(self,name):      
        self._name = name
        self._numbers = []
        self._address = ""
    
    def numbers(self):        
        return self._numbers
 
    def add_number(self,number:str):
        if number != "":
            self._numbers.append(number)
    
    def address(self):
        if not self._address:
            return None
        return self._address
    
    def add_address(self, address:str):
        self._address = address
 
    def name(self):
        return self._name
    
    def __str__(self) -> str:
        return f"name: {self._name}\nnumbers: {self._numbers}\naddress: {self._address}"
 
class PhoneBook:
    def __init__(self):
        self.__persons = {}
 
    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)        
        self.__persons[name].add_number(number)       
    
    def add_address(self,name:str, address:str):
        if not name in self.__persons and name != "":
            self.__persons[name] = Person(name)          
        self.__persons[name].add_address(address)
 
    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]
 
    def all_entries(self):        
        print(self.__persons)
 
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
 
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")
        print("4 print all")
 
    def add_number(self):
        name = input("name: ")
        number = input("number: ")        
        self.__phonebook.add_number(name, number)
 
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)
 
    def search(self):
        name = input("name: ")        
        data = self.__phonebook.get_entry(name)
        if data != None:        
            address = data.address()
            number = data.numbers()
            if len(number)==0:
                print("number unknown")
            for num in number:           
                print(num)
            print(address) if address != None else print("address unknown")
        else:
            print("number unknown")
            print("address unknown")
        
 
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()          
            else:
                self.help()
 
 
# when testing, no code should be outside application except the following:
phonebook = PhoneBookApplication()
phonebook.execute()
