print("****************************************************")
print("====== Welcome to My Personal Finance Tracker ======")
print("****************************************************")

print()
name = input ("What's your name?: ")
print(" Okay!!")
print()
income = float (input ("Enter the total income for next month: $"))
print(" Okay!!")
transport = float ( input ("What's the total expenses for transportation?: $"))
print(" Good!!")
feeding = float(input ("What's the total expenses for nutrition?: $"))
print(" Alright")
internet = float ( input (" How much will browsing & data cost?: $"))
print(" Good!! ")
saving = float (input ("What is your saving target?: $"))
print("perfect!!")

total_expenses = transport + feeding + internet
balance = income - total_expenses
saving_percentage = (saving/income)* 100
remainder = balance - saving

print("====== Final-track-down =======")
print()
print("Dear Mr. " ,name , "Your monthly salary is $",income )
print("Your total amount for expenses in the upcoming month is $" ,total_expenses)
print("After calculation, the balance is $", balance )
print("The percentage of saving is " , saving_percentage,"%")
print("The residual money from ur income is $" , remainder)





