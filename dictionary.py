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
        answer = input("Did you mean %s instead? Enter Y if yes and N if no: "  % get_close_matches(word, data.keys())[0])
        if answer.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif answer.lower() == 'n':
            return "The word does not exist. Double check the word"
        else:
            return "We did not understand the response"

    else:
        return "The word does not exist. Double check the word"

word = input('What word would you like to look up? ')
definition = dict_search(word)

if type(definition) == list:
    for definition in definition:
        print(definition)
else:
    print(definition)
