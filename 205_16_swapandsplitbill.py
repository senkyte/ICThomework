question = int(input("Select question:"))

if question == 1:
 A = (input("Select value of A:")) 
 B = (input("Select value of B:")) 
 temp = A 
 A = B 
 B = temp
 print("The value of A swapped is ",A)
 print("The value of B swapped is",B)
elif question == 2:
 TotalCost = int(input("Please choose total cost (SGD):"))
 Amt = int(input("Please select the amount of people:"))
 SplitBill= (TotalCost/Amt)
 GST = int(input("Please input GST (if you want to exclude, please type 0):"))
 GSTPrice = (GST/100 * SplitBill)
 SC = int(input("Select Service Charge, if you want to exclude, type 0:"))
 SCPrice = (SC/100 * SplitBill)
 TotalDeduction = (SCPrice + GSTPrice)
 print("The total price you have to pay is", SplitBill+TotalDeduction)
elif question > 2:
 print("Choose either 1 or 2!")

