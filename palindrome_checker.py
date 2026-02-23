text = input("Enter word/number: ")

rev = ""
length = len(text)

print("\nReversing process:")

# reverse one character at a time
for i in range(length - 1, -1, -1):
    rev = rev + text[i]
    print("Current reversed value:", rev)

print("\nOriginal:", text)
print("Reversed:", rev)


if text.lower() == rev.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")