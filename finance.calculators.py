import math
print ("investment - to calculate the amount of interest you'll earn on your investment \nbond - to calculate the amount you'll have to pay on a home loan")
user_input= input("Enter either 'investment' or 'bond' from the menu above to proceed: \n")
user_input= user_input.lower ()

#gets input from user
if user_input== "investment":
    p =int (input ("Please enter how much you are depositing?: "))
    r= int (input ("Please enter the interest rate as a percentage (number only): "))/100
    t= int (input ("How many years are you investing for?: "))
    user_interest= input ("Do you want simple or compound interest?: ")

    #calculates interest
    if user_interest== "simple":
        a = p*(1 + r*t)
        print ("You total interest will be: ", a)
    elif user_interest== "compound":
        a = p * math.pow((1+r),t)
        print ("You total interest will be: ", a)
if user_input== "bond": #calculates bond rate
    P= float (input ("Please enter the value of your house?: "))
    i= (float (input ("Please enter the interest rate?: "))/100)/12 #diving the interst rate as user enetering full numberand  dividing by months in year to get 1 month
    n= int (input("Number of months for repayement?: "))
    repayment = (i * P)/(1 - (1 + i)**(-n))
    print (f"You will repay {repayment} every month")
else:
    print ("User input error!")



