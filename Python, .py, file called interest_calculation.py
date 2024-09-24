InvestmentIsValid = False
IntrestRateIsValid = False
InvestmentDurationIsValid = False
Investment = int(input("Enter an investment amount between $0 - $50,000, "))
while InvestmentIsValid == False: 
   if Investment < 0 or Investment > 50000:
      print("You entered an investment number below $0 or more than $50,000")
      Investment = int(input("Please enter a valid investment amount, "))
   else:
      InvestmentIsValid = True

IntrestRate = int(input("Enter an intrest rate between 04-154,"))
while IntrestRateIsValid== False:
    if IntrestRate < 0 or IntrestRate > 15:
       print("You entered an intrest below 04 or higher than 154")
       IntrestRate = int(input("Please enter a valid intrest rate"))
    else:
        IntrestRateIsValid = True
InvestmentDuration = int(input("Enter an Investment duration in years above 0,"))
while InvestmentDurationIsValid == False:
    if InvestmentDurationIsValid <=0:
       print("You entered an investment duration in years below or 0")
       InvestmentDuration = int(input("Please enter a valid duration, "))
    else:
        InvestmentDurationIsValid = True 
IntrestRate = IntrestRate / 12
IntrestRate = IntrestRate / 100
InvestmentAmount = Investment
for Years in range (1,InvestmentDuration +1):
     for Month in range (1, 12+1):
         InvestmentAmountAdd = InvestmentAmount + IntrestRate 
         InvestmentAmount = InvestmentAmount + InvestmentAmountAdd
    print("Year", Years, ", 5" + str (round(InvestmentAmount,2)))


   




