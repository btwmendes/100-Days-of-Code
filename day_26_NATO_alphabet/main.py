
#TODO 1. Create a dictionary

with open("./nato_phonetic_alphabet.csv") as file:
    nato = file.readlines()
alphabet_list = [item.split(",") for item in nato]
alphabet = {item[0]: item[1].strip() for item in alphabet_list}
# print(alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ")
word_list = [alphabet[letter.upper()] for letter in word ]
print(word_list)
