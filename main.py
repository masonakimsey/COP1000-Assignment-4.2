nameInput = input("Employee's name: ")
shiftInput = input("Number of Shifts: ")
transactionInput = input("Number of transactions: ")
valueInput = input("Transaction dollar value: ") 
bonus = 0

productivityScore = (float(valueInput) / float(transactionInput)) / float(shiftInput)

if productivityScore <= 30:
  bonus = 50.00
if 30 < productivityScore < 70:
  bonus = 75.00
if 69 < productivityScore < 200:
   bonus = 100.00
if productivityScore >= 200:
  bonus = 200.00

print (str("Employee name: ") + nameInput)
print (str("Employee Bonus: $") + str(bonus))