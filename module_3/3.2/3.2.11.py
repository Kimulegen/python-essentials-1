user_word = input("Enter a word")
user_word = user_word.upper()

vowels = ["A", "E", "I", "O", "U"]
word_without_vowels = ""

for letter in user_word:
    if letter in vowels:
        continue
    word_without_vowels += letter

print(word_without_vowels)
