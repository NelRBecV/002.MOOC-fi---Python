# WRITE YOUR SOLUTION HERE:
class ListHelper:
 
    @classmethod
    def greatest_frequency(cls,numbers:list):
        """Returns the number that reapeats most in list.""""
      
        greatest = [0,0]
        for m in numbers:
            counter = 0
            for n in numbers:
                if m == n:
                    counter +=1
            if counter > greatest[1]:
                greatest[0] = m
                greatest[1] = counter
        return greatest[0]
 
    @classmethod
    def doubles(cls, numbers:list):
        """Returns the numbers who repeats twice or more in list."""
      
        doubles = []
        for m in numbers:
            counter = 0
            for n in numbers:
                if n == m:
                    counter += 1
            if counter >= 2 and m not in doubles:
                doubles.append(m)
        return len(doubles)
 
if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))



