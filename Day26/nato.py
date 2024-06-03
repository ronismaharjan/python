import pandas


data = pandas.read_csv("Day26/nato_phonetic_alphabet.csv")

data_dict = {name.letter:name.code for (data, name) in data.iterrows()}

user = input("Enter a word: ").upper()
user_nato =[f"{letter}:{data_dict[letter]}" for letter in user]

print(user_nato)
