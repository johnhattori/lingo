#!/usr/bin/env python3

import random

WORD_FILE = 'words.txt'

def main():
    words = extract_words(WORD_FILE)
    done = False
    while not done:
        target = get_random_word(words)
        playing = True
        while playing:
            guess = get_guess_word()
            if guess == target:
                print("You've won")
                playing = False
            else:
                score = get_score(target, guess)
                colored = color_score(score)
                print(colored)

def get_guess_word():
    return input("Enter a five letter word: ")

def color_score(score):
    return score

def get_score(target, guess):
    assert len(target) == len(guess)
    tlist = list(target.lower())
    glist = list(guess.lower())
    for index, char in enumerate(glist):
        if char == tlist[index]:
            glist[index] = char.upper()
            tlist[index] = ""
    for index, char in enumerate(glist):
        if char not in tlist and char != glist[index].upper():
            glist[index] = "-"
        elif char in tlist:    
            tlist[tlist.index(char)] = ""
            
    return ''.join(glist)    

def extract_words(file_path):
    with open(file_path) as fh:
        words = fh.read().strip().split(' ')        
    return words

def get_random_word(words):
    return random.choice(words)

if __name__ == "__main__":
    main()
    """
    print(get_score('a', 'a'), 'A')
    print(get_score('a', 'b'), '-') 
    print(get_score('ab', 'ab'), 'AB')
    print(get_score('ab', 'ba'), 'ba')
    print(get_score('abc', 'cba'), 'cBa')
    print(get_score('abc', 'def'), '---')
    print(get_score('aa', 'ba'), '-A')
    print(get_score('ab', 'aa'), 'A-')
    print(get_score('algal', 'agagk'), 'Aga--')
    """

