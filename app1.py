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
    elif w.title() in data:
        return data[w.title()] #If user enters names of states or cities in lowercase like texas, it will convert it to Texas and check
    elif w.upper() in data:  # If user enters acronyms like USA
        return data[w.upper()] 
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter y if yes, or n if no: " % get_close_matches(w,data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "n":
            return "In that case, the word does not exist. "
        else:
            return "Sorry but we did not understand your entry. "
    else:
        return("Sorry, but either the word does not exist, or it's not in our dictionary. Please recheck.\n")

word = input("Please enter a word.\n")

output = meaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
