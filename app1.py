# import json
#
# data = json.load(open("data.json"))
#
# def translate(word):
#     if word in data:
#         return data[word]
#
#     else:
#         return("Sorry, but either the word does not exist, or it's not in our dictionary. Please try another one.\n")
#
# word = input("Enter a word: ")
#
# print(translate(word))


import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))
def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]
    else:
        return("Sorry, but either the word does not exist, or it's not in our dictionary. Please recheck.\n")

word = input("Please enter a word.\n")

print(meaning(word))
