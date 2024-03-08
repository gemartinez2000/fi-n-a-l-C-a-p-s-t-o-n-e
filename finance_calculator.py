import math

#showcases a menu and gives the user a choice
print("Menu:")
print("1. Investment - calculate interest")
print("2. Bond - calculate monthly bond repayment ")
choose = input("Enter either 'investment' or 'bond': ").lower()

#find if it was one of the options the user could have choosen
if choose == "investment": 
    #user will enter the details related to the investment
    principal = float(input("Enter the initial amount of money being invested: "))
    rate = float(input("Enter the interest rate at which will be invested (as a percentage):")) / 100
    years = int(input("Enter years the investment will last: "))
    type_interest_rate = input("Enter 'simple' or 'compund' interest being used in the investment: ")

    #use the type of interest to calculate end result
    if type_interest_rate == "simple":
        interest = principal * (1 + rate * years)
    elif type_interest_rate == "compound":
        interest = principal * (1 + rate) ** years
    else:
        print("Invalid interest type.")
        exit(1)
    
    #show result after investment period
    print(f"Your {type_interest_rate} interest after {years} years will be: {interest:.2f}")

elif choose == "bond":
    #insert bond details
    face_value = float(input("Enter the present value of the bond: "))
    rate_bond = float(input("Enter the interest (as percentage): ")) / 100
    months = int(input("Duration of the bond in months: "))
    
    #calculation of the bond value
    monthly_interest_bond = (rate_bond / 12 * face_value) / (1 - (1 + rate_bond / 12) ** - months)
    
    #print the end result of the bond
    print(f"Your monthly bond repayment will equal: :{monthly_interest_bond:.2f}")

else:
    print("Invalid decision. Select either a 'investment' or 'bond' . ")




                            