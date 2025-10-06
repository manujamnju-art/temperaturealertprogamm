temp = int(input("Enter the temperature:"))
if temp<=20:
    print("Cold")
elif temp<=35:
    print("Normal")
else:
    print("Hot")

celsius = int(input("Enter the temperature in celsius:"))
fahrenheit = (celsius * 9/5) + 32
print("The celsius degree in fahrenheit is:",fahrenheit)

