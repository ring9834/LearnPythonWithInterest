rainy = input("What's the weather like today？Any rain？（y/n）").lower()
cold  = input("Is it cold outside？（y/n）").lower()
if (rainy == 'y' and cold == 'y'):
    print("You'd better take a raincoat！")
if (rainy == 'y' and cold != 'y'):
    print("You'd better take an umbrella！")
if (rainy != 'y' and cold == 'y'):
    print("It's cold outside, you need a coat！")
if (rainy != 'y' and cold != 'y'):
    print("It depends to wear what kinds of clothe，the scenary is so beautiful outside！")
