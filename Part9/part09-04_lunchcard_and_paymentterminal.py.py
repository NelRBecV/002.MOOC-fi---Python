# WRITE YOUR SOLUTION HERE:
	 
	class LunchCard:
	    def __init__(self, balance: float):
	        self.balance = balance
	 
	    def deposit_money(self, amount: float):
          """Increment card's balance."""
	        self.balance += amount
	 
	    def subtract_from_balance(self, amount: float):
          """Discount the introduced amount from balance."""
	        if self.balance >= amount:
	            self.balance -= amount
	            return True
	        return False
	        # The amount should be subtracted from the balance only if there is enough money on the card
	        # If the payment is successful, the method returns True, and otherwise it returns False
	 
	class PaymentTerminal:
	    def __init__(self):
	        # Initially there is 1000 euros in cash available at the terminal
	        self.funds = 1000
	        self.lunches = 0
	        self.specials = 0
	 
	    def eat_lunch(self, payment: float):        
	        # A regular lunch costs 2.50 euros.
	        # Increase the value of the funds at the terminal by the price of the lunch,
	        # increase the number of lunches sold, and return the appropriate change.
	        # If the payment passed as an argument is not large enough to cover the price,
	        # the lunch is not sold, and the entire sum is returned.
	        regular_price:float = 2.50
	        if not payment > regular_price:
	            return payment
	        self.funds += regular_price
	        self.lunches += 1
	        return round(payment - regular_price,1)
	 
	    def eat_special(self, payment: float):
	            # A special lunch costs 4.30 euros.
	            # Increase the value of the funds at the terminal by the price of the lunch,
	            # increase the number of specials sold, and return the appropriate change.
	            # If the payment passed as an argument is not large enough to cover the price,
	            # the lunch is not sold, and the entire sum is returned.
	            special_price:float = 4.30
	            if payment < special_price:
	                return payment
	            self.funds += payment
	            self.specials +=1
	            return payment - special_price
	 
	    def eat_lunch_lunchcard(self, card: LunchCard):
	        # A regular lunch costs 2.50 euros.
	        """Return True if there is enough money on the card and subtract the price of the lunch from the balance.
	        Otherwise, return False."""
	        regular_lunch:float = 2.5
	        if not card.balance >= regular_lunch:
	            return False
	        card.balance -= regular_lunch
	        self.lunches +=1
	        return True
	 
	    def eat_special_lunchcard(self, card: LunchCard):
	        # A special lunch costs 4.30 euros.
	        """Return True if there is enough money on the card and subtract the price of the lunch from the balance.
	        Otherwise, return False."""
        
	        special_lunch:float = 4.3
	        if card.balance < special_lunch:
	            return False
	        card.balance -= special_lunch
	        self.specials += 1
	        return True
	 
	    def deposit_money_on_card(self, card: LunchCard, amount: float):
	        if amount >= 0:
	            self.funds += amount
	            card.balance += amount
	        
	 
	if __name__=="__main__":
	    exactum = PaymentTerminal()
	 
	    card = LunchCard(2)
	    print(f"Card balance is {card.balance} euros")
	 
	    result = exactum.eat_special_lunchcard(card)
	    print("Payment successful:", result)
	 
	    exactum.deposit_money_on_card(card, 100)
	    print(f"Card balance is {card.balance} euros")
	 
	    result = exactum.eat_special_lunchcard(card)
	    print("Payment successful:", result)
	    print(f"Card balance is {card.balance} euros")
	 
	    print("Funds available at the terminal:", exactum.funds)
	    print("Regular lunches sold:", exactum.lunches)
	    print("Special lunches sold:", exactum.specials)
	 
