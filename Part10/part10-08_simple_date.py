# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    """This class emulates how "datetime" class works. A notorious differences can be seen in years an months.
    
        A year is taken as 360 days and months are all rounded by 30."""
  
    def __init__(self, day: int, month: int, year: int):
        self.day: int = day
        self.month: int = month
        self.year: int = year
        self.check_inputs(day,month)
 
    def check_inputs(self, day: int, month: int):
        if 0 < day > 30 and 0 < month > 12:
            raise ValueError("data input is not a date")
 
    def date_in_days(self, date: "SimpleDate"):
        year: int = date.year * 360
        month: int = date.month * 30       
        days: int = date.day + month + year
        return days
 
    def date_transform(self, days: int):
        """Transforms an amount of days into a date."""
      
        year: float = days/360        
        new_year: float = year - int(year)
        month: int = new_year * 12        
        new_month: float = month - int(month)        
        day: int = round(new_month * 30)
 
        return day, int(month), int(year)
 
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
 
    def __gt__(self, date: "SimpleDate"):
        if self.year > date.year:
            return True
        elif self.month > date.month and self.year == date.year:
            return True
        elif self.day > date.day and self.year == date.year and self.month==date.month:
            return True
        else:
            return False
 
    def __lt__(self, date:"SimpleDate"):
        if self.year < date.year:
            return True
        elif self.month < date.month and self.year == date.year:
            return True
        elif self.day < date.day and self.year == date.year and self.month == date.month:
            return True
        else: 
            return False
 
    def __eq__(self, date:"SimpleDate"):
        return self.year == date.year and self.month == date.month and self.day == date.day
 
    def __ne__(self, date:"SimpleDate"):
        return self.year != date.year or self.month != date.month or self.day != date.day
 
    def __add__(self, days:int):
        current_date = self.date_in_days(self)
        new_date = current_date + days
        day,month,year = self.date_transform(new_date)
        return SimpleDate(day, int(month), int(year))
 
    def __sub__(self, date:"SimpleDate"):
        current_date = self.date_in_days(self)
        another_date = self.date_in_days(date)        
        new_date = current_date - another_date               
        return abs(new_date)
 
 
if __name__ == "__main__":
 
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)
 
    print(d2 - d1)
    print(d1 + d2)
    print(d1 - d3)



