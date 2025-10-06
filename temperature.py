temperature = float(input("Enter the temperature in Celsius: "))

if temperature < 20:
    print("It's cold ")
elif 20 <= temperature <= 30:
    print("It's normal ")
else:
    print("It's hot ")
