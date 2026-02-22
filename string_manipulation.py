sentence = input("Enter a sentence: ").strip()

print("Original sentence:", sentence)
print("Total Characters (with space):",len(sentence))

#Replacing white space - " " with "" (no space) to calculate total characters without space
print("Total Characters (without space):",len(sentence.replace(" ","")))

#Splitting the sentence using split() and finding the length of the resulting list to get the total number of words.
words = sentence.split()
print("Total Words:",len(words))

print("UPPERCASE:",sentence.upper())

print("lowercase:",sentence.lower())

print("Title Case:",sentence.title())

#Printing the first word of the sentence
first_word = ""   # to store characters of the first word as strings cannot be appended directly
for i in sentence:
    if i !=" ":
        first_word+=i
    else:
        break

print("First Word:",first_word) 

#Printing the last word of the sentence
last_word = sentence.split()[-1]
print("Last Word:", last_word)

#Printing reversed sentence
print("Reversed:",sentence[::-1])



