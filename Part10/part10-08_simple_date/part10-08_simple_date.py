# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
        self.check_inputs(day, month)

    def check_inputs(self, day: int, month: int):
        if 0 < day > 30 and 0 < month > 12:
            raise ValueError("data input is not alid")

    def __date_in_days(self):
        year = self.year * 360
        month = self.month * 30
        days = self.day + month + year
        return days

    def __date_transform(self, days: int):
        year = days / 360
        new_year = year - int(year)
        month = new_year * 12
        new_month = month - int(month)
        day = round(new_month * 30)

        return day, int(month), int(year)

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __gt__(self, date: "SimpleDate"):
        if self.year > date.year:
            return True
        elif self.month > date.month and self.year == date.year:
            return True
        elif self.day > date.day and self.year == date.year and self.month == date.month:
            return True
        else:
            return False

    def __lt__(self, date: "SimpleDate"):
        if self.year < date.year:
            return True
        elif self.month < date.month and self.year == date.year:
            return True
        elif self.day < date.day and self.year == date.year and self.month == date.month:
            return True
        else:
            return False

    def __eq__(self, date: "SimpleDate"):
        return self.year == date.year and self.month == date.month and self.day == date.day

    def __ne__(self, date: "SimpleDate"):
        return self.year != date.year or self.month != date.month or self.day != date.day

    def __add__(self, days: int):
        new_date = self.__date_in_days() + days
        day, month, year = self.__date_transform(new_date)
        return SimpleDate(day, int(month), int(year))

    def __sub__(self, date: "SimpleDate"):
        return abs(self.__date_in_days() - date.__date_in_days())


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2 - d1)
    print(d1 + 40)
    print(d1 - d3)
