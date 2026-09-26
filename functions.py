def main() :
    #call area calculation function
    circleArea = areaCalc(float(input("Enter the Radius of this Circle: ")))
    #format to have 2 decimals
    circleAreaFormatted =  f"{circleArea:.2f}"
    print("Output: ", circleAreaFormatted)

    #amount and tax rate
    amount = float(input("Enter the amount of money before tax: "))
    taxInput = (input("Enter the tax rate: "))
    #remove the % from the input
    taxRate = float(taxInput.strip('%'))

    #call tax calculation function
    taxTotal = taxCalc(amount, taxRate)
    #format to have 2 decimals
    taxTotalFormatted = f"{taxTotal:.2f}"
    print("Output: ", taxTotalFormatted)
 
    #call temperature conversion function
    tempInput = float(input("Enter the temperature in Fahrenheit: "))
    print("Output: ", tempConv(tempInput))

def areaCalc(radius) :
    Pi = 3.14159
    return Pi * (radius ** 2)

def taxCalc(amount, taxRate) :
    return amount + (amount * (taxRate / 100))

def tempConv(temp) :
    return (temp - 32) * (5/9)
    
main()