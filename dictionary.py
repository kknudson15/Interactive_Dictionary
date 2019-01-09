'''
This is an interactive dictionary
'''

import json
from difflib import SequenceMatcher, get_close_matches
data = json.load(open("data.json"))

def dict_search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(word, data.keys())[0]
    else:
        return "The word does not exist. Double check the word"

word = input('What word would you like to look up?')
definition = dict_search(word)
print(definition)
