print("Welcome to the Unit Converter!")
while True:
    unit = input("What unit are you using? (m/s <-> km/h or Celsius <-> Fahrenheit)").lower()
    if unit == "exit":
        print("Thanks for using the Unit Converter!")
        break
    elif unit == "km/h":
        speedkmph = input("How fast are you going in Km/h? ")
        unitmps = float(speedkmph) * 0.27778
        print("The speed in Mp/s is: " + str(unitmps) + " (Type 'exit' to exit)")
    elif unit == "m/s":
        speedmps = input("How fast are you going in M/s? ")
        unitkmph = float(speedmps) * 3.6
        print("The speed in Km/h is: " + str(unitkmph) + " (Type 'exit' to exit)")
    elif unit == "celsius":
        tempcelsius = input("What is the temperature in Celsius? ")
        unitfahrenheit = float(tempcelsius) * 9 / 5 + 32
        print("The temperature in Fahrenheit is: " + str(unitfahrenheit) + " (Type 'exit' to exit)")
    elif unit == "fahrenheit":
        tempfahrenheit = input("What is the temperature in Fahrenheit? ")
        unitcelsius = (float(tempfahrenheit) -32) * 5 / 9
        print("The temperature in Celsius is: " + str(unitcelsius) + " (Type 'exit' to exit)")
    else:
        print("Please type a unit above")