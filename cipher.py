abc = "abcdefghijklmnoplqrstuvwxyz"
shift = 5
text = input("Please enter a sentence: ")
text = text.lower()

encrypt = ""

for char in text:
    if char in abc: 
        index = abc.find(char)
        index = (index + shift) % 26
        char = abc[index]
    encrypt += char

print("The encrypted message is", encrypt)