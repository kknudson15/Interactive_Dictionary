'''
This is an interactive dictionary Program
built by Kyle Knudson, 2019
Built while working through UDEMY course

The user is able to enter a word and the dictionary returns the definition 
or multiple definitions depending upon the number of definitions that the 
word has. 
The dictionary also uses close matches to offer suggestions to the user
to help deal with misspellings.  
'''

import json
from difflib import SequenceMatcher, get_close_matches
#Reads in the data from the data.json file to a python dictionary
data = json.load(open("data.json"))


def dict_search(word):
    '''
    The function handles the lookup of the word that the user enters.
    The function handles proper nouns, incorrect entries and offers
    suggestions if the input closely matches something in the data.
    
    Inputs: A string word that the user is trying to lookup
    Outputs: returns a list of definitions or a string with a message
    '''
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
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

#main program operation
word = input('What word would you like to look up? ')
definition = dict_search(word)

#Output optimization
if type(definition) == list:
    for definition in definition:
        print(definition)
else:
    print(definition)
