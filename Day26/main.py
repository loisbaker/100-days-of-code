

import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

input_word = input('Enter a word: ').upper()
try:
    code_list = [nato_dict[letter] for letter in input_word]
except KeyError:
    raise KeyError("Sorry, only letters in the alphabet please")
else:
    print(code_list)
