# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
 
    def _separated_to_float(self,value1:int, value2:int):        
        total_value = value1 + (value2 / 100)        
        return total_value
 
    def _get_toghether(self, value:float):
        values = str(value).split(".")
        if len(values[1])==1:
            values[1] += "0"
        return values[0], values[1]
 
    def __str__(self):
        return f"{self.__euros}.{self.__cents:>02} eur"
 
    def __eq__(self,another:"Money"):
        return self._separated_to_float(self.__euros, self.__cents) == self._separated_to_float(another.__euros,another.__cents)
        
    def __lt__(self, another:"Money"):
        return self._separated_to_float(self.__euros,self.__cents) < self._separated_to_float(another.__euros,another.__cents)
    
    def __gt__(self, another: "Money"):
        return self._separated_to_float(self.__euros,self.__cents) > self._separated_to_float(another.__euros,another.__cents)
 
    def __ne__(self, another: "Money"):
        return self._separated_to_float(self.__euros,self.__cents) != self._separated_to_float(another.__euros,another.__cents)
 
    def __add__(self, another: "Money"):
        total = self._separated_to_float(self.__euros, self.__cents) + self._separated_to_float(another.__euros,another.__cents)                        
        euros, cents = self._get_toghether(total)
        return Money(int(euros),int(cents))
 
    def __sub__(self, another:"Money"):
        total = self._separated_to_float(self.__euros,self.__cents) - self._separated_to_float(another.__euros,another.__cents)
        if total < 0:
            raise ValueError("negative values is not allowed")
        euros, cents = self._get_toghether(round(total,2))
        return Money(int(euros),int(cents))
 
if __name__ == "__main__":
    money1 = Money(15, 95)
    money2 = Money(15, 95)
 
    e3 = money1 + money2
    e4 = money1 - money2 
    
    print(e3)
    print(e4)
 
    
	 



