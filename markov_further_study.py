"""Work on creating the dictionary comprehension"""

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


def make_chains(text_string,n=2):
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
    string_list = text_string.split() + ['my_very_special_last_word']

    for i in range(0, len(string_list)- n +1):
        #     
        if i == len(string_list)-n:
            if tuple(string_list[i:n + i]) in chains:
                chains[tuple(string_list[i:len(string_list)])].append('')
            else: 
                chains[tuple(string_list[i:len(string_list)])] = ['']

        else:
            if tuple(string_list[i:n + i]) in chains:
                chains[tuple(string_list[i:i+n])].append(string_list[i+n])
            else: 
                chains[tuple(string_list[i:i+n])] = [string_list[i+n]]


    # for keys in chains:
    #     chains[keys] = list(set(chains[keys]))
    #print('dictionary', chains)
            
    # dictionary containing key:value for every key where the key is a tuple(ngram) and value 
    # is a list of next words  
def make_chain2(text_string,n=2): 

    # your code goes here
    string_list = text_string.split() + ['my_very_special_last_word']
    print ({
        tuple(string_list[i:i+n]):list(string_list[i+n]) 
        for i in range(0, len(string_list-n))})

    return None




def make_text(chains):
    """Return text from chains."""

    random_string = ''
    starting_word = choice([key for key in chains if key[0][0].isupper()])
    #starting_word = choice(list(chains))
    key_word = starting_word
    for word in starting_word:
        random_string += word + ' '
        #'{} {}'.format(starting_word[0], starting_word[1])

    while True:
        next_word = choice(chains[key_word])
        key_word = (key_word[1:]) + (next_word,)
        random_string += next_word + ' '
        if next_word == 'my_very_special_last_word':
            break

    #words = []
    # your code goes here

    return random_string
    #return " ".join(words)


input_path = sys.argv[1]
input_n = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
#chains = make_chains(input_text, input_n)
chains2 = make_chain2(input_text, input_n)
# Produce random text
random_text = make_text(chains2)

print(random_text)
