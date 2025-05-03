
values = { #adding a dictionary with values of each coin
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25,
    'pennie': 0.01 #added this case to address the suffix
}

def parser(sentence): #parses the inputted sentence and calculates the total
    total = 0
    chunks = sentence.split(" and ") #split the sentence by phrase

    for chunk in chunks:
        words = chunk.strip().split() #separates the name of the coin and the amount

        if len(words) >= 2: #processes only phrases
            quantity = int(words[0])
            coin = words[1].lower()

            coin = coin.removesuffix('s') #using string method to remove suffix from end of coin

            if coin in values: #add coin value to total
                total += quantity * values[coin]
    return f"{total:.2f}" #return final total to 2 decimal places


print(parser("1 penny and 2 nickels"))
print(parser("4 dimes and 7 quarters "))
print(parser("1 quarter and 3 pennies"))
print(parser("21 pennies and 17 dimes and 52 quarters"))
print(parser("95 dimes and 73 quarters and 22 nickels and 36 pennies"))
print(parser("1 nickel and 17 quarters "))
print(parser("21 nickels and 15 pennies"))
print(parser("3 dimes and 2 nickels"))

