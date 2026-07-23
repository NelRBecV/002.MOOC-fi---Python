# Write your solution here
eat_cafe = int(input("How many times a week do you eat at the student cefeteria?"))
lunch_price = float(input("The price of a typical student lunch?"))
money_spend = float(input("How much money do you spend on groceries in a week?"))
average_spend = (eat_cafe*lunch_price) + money_spend

print("\nAverage food expenditure:")
print(f"Daily: {average_spend/7} euros")
print(f"Weekly: {average_spend} euros")
