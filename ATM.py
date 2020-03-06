
    
correct_pin = 1006
print("Welcome to OB Bank ATM")
pin = int(input("Please enter your 4 digit pin:"))
tries = 1
balance=500
withdrawals = 1
while correct_pin == 1006:
    if tries < 3 and pin!= correct_pin:
        tries+=1
        pin=int(input("Wrong pin, Re-Enter pin again:"))
        if tries == 3 and pin!= correct_pin:
            print("Incorrect pin, you have no remaining attempts to input your pin!")
            
    else:
        if pin == correct_pin and tries < 4:
            print("Correct pin, You are Welcome")
            print("You have $500 in your account")
            if pin == correct_pin and withdrawals < 3:
                withdrawals+=1
                cash=int(input("Please enter amount to withdraw:"))
                print("Please take cash")
                print("Your cash balance is ${}".format(balance-cash))
                print("Thank you for banking with us")
            else:
                print("You have exceeded your withdraw limit")
                correct_pin = False
    


    

