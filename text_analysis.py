# count words
def count_words(text):
    words = text.split()
    return len(words)


# count vowels
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count = count + 1
    return count


# count consonants
def count_consonants(text):
    count = 0
    for ch in text.lower():
        if ch.isalpha() and ch not in "aeiou":
            count = count + 1
    return count


# reverse text
def reverse_text(text):
    rev = ""
    for i in range(len(text) - 1, -1, -1):
        rev = rev + text[i]
    return rev


# check palindrome
def is_palindrome(text):
    t = text.replace(" ", "").lower()
    rev = ""
    for i in range(len(t) - 1, -1, -1):
        rev = rev + t[i]
    if t == rev:
        return True
    else:
        return False


# remove vowels
def remove_vowels(text):
    new_text = ""
    for ch in text:
        if ch.lower() not in "aeiou":
            new_text = new_text + ch
    return new_text


# word frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}

    for w in words:
        if w in freq:
            freq[w] = freq[w] + 1
        else:
            freq[w] = 1

    return freq


# longest word
def longest_word(text):
    words = text.split()
    long_word = ""

    for w in words:
        if len(w) > len(long_word):
            long_word = w

    return long_word, len(long_word)


# main function
def analyze_text(text):

    print("\n=== TEXT ANALYSIS ===")

    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))

    lw, length = longest_word(text)
    print("Longest word:", lw, "(", length, "letters )")

    freq = word_frequency(text)

    print("Word Frequency:", end=" ")
    for key in freq:
        print(key + ":", freq[key], end=", ")


# input
text = input("Enter text: ")
analyze_text(text)