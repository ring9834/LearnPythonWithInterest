message = input("Please input an English sentence：")
message = message.upper()
output = ""
for letter in message:
    if letter.isupper():
        value = ord(letter) + 13
        letter = chr(value)
        if not letter.isupper():
            value -= 26
            letter = chr(value)
    output += letter
print("The output result is：",output)
