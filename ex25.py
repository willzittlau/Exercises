def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first(words):
    word = words.pop(0)
    print (word)
    
def print_last(words):
    word = words.pop(-1)
    print (word)
    
def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first(words)
    print_last(words)
    
def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first(words)
    print_last(words)

