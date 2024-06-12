def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

totalPrice = int(input("Total Price is: "))

print("Your Total Price with vat is:", vatCalculate(totalPrice))