"""Maybe start on a new function for n-length keywords, instead of trying to edit thse"""
"""use existing dictionary and keep adding from the values of the keys until our k has n words in it"""


"""Generate Markov text from text files."""
from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_object = open(file_path)
    #file_object.read() 
    #print (file_object)

    # join_string = ""

    # for line in file_object:
    #     line = line.rstrip() 
    #     join_string = join_string + line + " "



    return file_object.read()
    #print (join_string)
    #return join_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here

    string_list = text_string.split()
    for i in range(0, len(string_list)-1):
        if i == len(string_list)-2:
            chains[(string_list[i], string_list[i+1])] = []
        else:
            if (string_list[i], string_list[i+1]) in chains:
                chains[(string_list[i], string_list[i+1])].append(string_list[i+2])
            else: 
                chains[(string_list[i], string_list[i+1])] = [string_list[i+2]]


    for keys in chains:
        chains[keys] = list(set(chains[keys]))
    
    print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""



    starting_word = choice(list(chains))
    key_word = starting_word
    random_string = '{} {}'.format(starting_word[0], starting_word[1])

    while chains[key_word] != []:
        next_word = choice(chains[key_word])
        key_word = (key_word[1], next_word)
        random_string = '{} {}'.format(random_string, next_word)
    #words = []
    # your code goes here
    return random_string
    #return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
