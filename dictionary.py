'''
This is an interactive dictionary
'''

import json
data = json.load(open("data.json"))

def dict_search(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word does not exist. Double check the word"

word = input('What word would you like to look up?')
definition = dict_search(word)
print(definition)
