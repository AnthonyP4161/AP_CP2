#AP 2nd Period, Financial Calculator
#saving times function
def savings():
    goal = float(input("Alrighty, how much are you saving: "))
    print("How often are you gonna be contributing? Type the number for the related option\n1) Weekly\n2) Monthly")
    while True:
        placeholder = input("Enter Here: ")
        if placeholder == "1":
            placeholder = "weeks"
            break
        elif placeholder == "2":
            placeholder == "months"
            break
        else:
            print("What the flippity flip. These are your options, enter the number\n1) Weekly\n2) Monthly")
    contributing = int(input("Alrighty, so how much are you gonna contribute each time: "))
    time = goal/contributing
    print(f" It will take {time} {placeholder} to save {goal}")
    print("Would you like to use the calculator again, yes or no")
#compound interest function
def compound():
    start = input("Alrighty, what is your starting amount: ")
    rate = input("What percentage is your interest rate, EX 5: ")
    rate = rate/100
    rate = rate+1
    time = input("How many years has it been spent compounding, EX 10: ")
    for i in time:
        number = start * rate
        start = number
    print(round(start,2))
#budget allocator function
def budget():
    print()
#sale price function
def sale_price():
    price = float(input("What is the original price of the item: "))
    discount = float(input("What is the discount of the item? Enter a whole number EX. 12: "))
    discount = 1-discount
    sale_price = price*discount
    print(f"The sales prices is {round(sale_price,2)}")
#tip function
def tip():
    price = float(input("What is the original price of the item: "))
    discount = float(input("What percentage are you tipping? Enter a whole number EX. 12: "))
    discount = discount/100
    tip = price*discount
    discount = 1+discount
    sale_price = price*discount
    print(f"The tip is {round(tip,2)} so the total price is {round(sale_price,2)}")
#start menu function
def start():
    def loopity_loop():
        print("Would you like to use the calculator again, yes or no")
        while True:
            placeholder = input("Enter Here: ").lower().strip()
            if placeholder == "yes":
                start()
            elif placeholder == "no":
                break
            else:
                print("What the flippity flip. Type yes or no")
    print("Hello, welcome to the financial calculator. Type the number for the related option\n1) Saving Times Calculator\n2) Compound Interest Calculator\n3) Budget Allocator\n4) Sales Price Calculator\n5) Tip Calculator")
    while True:
        placeholder = input("Enter Here: ")
        if placeholder == "1":
            savings()
            loopity_loop()
            break
        elif placeholder == "2":
            compound()
            loopity_loop()
            break
        elif placeholder == "3":
            budget()
            loopity_loop()
            break
        elif placeholder == "4":
            sale_price()
            loopity_loop()
            break
        elif placeholder == "5":
            tip()
            loopity_loop()
            break
        else:
            print("What the flippity flip. These are your options, enter the number\n1) Saving Times Calculator\n2) Compound Interest Calculator\n3) Budget Allocator\n4) Sales Price Calculator\n5) Tip Calculator")
start()