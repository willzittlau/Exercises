var1 = float(input("Enter the first number for addition:\n")) 
var2 = float(input("Enter the second number for addition:\n" ))
sum = var1+var2
print (int(sum))
Q = input("would you like to add a third number? (Y/N)\n")
if Q == "Y":
    var3=float(input("enter the number"))
    sum = sum+var3
    print (int(sum))
elif Q == "N":
    print("Finished")
else:
    print("Invalid Input\n")