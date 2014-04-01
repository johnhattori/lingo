#!/usr/bin/env python3

def main():

    done = False
    while not done:
        target = get_random_word()
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
            
def get_score(target, guess):
    print(target, guess, end=" : ")

    assert len(target) == len(guess)
    tlist = list(target)
    glist = list(guess)
    for index, char in enumerate(glist):
        if char == tlist[index]:
            glist[index] = char.upper()
            tlist[index] = ""
    for index, char in enumerate(glist):
        if char not in tlist and char != glist[index].upper():
            glist[index] = "-"
            
    return ''.join(glist)    

if __name__ == "__main__":
    print(get_score('a', 'a'), 'A')
    print(get_score('a', 'b'), '-') 
    print(get_score('ab', 'ab'), 'AB')
    print(get_score('ab', 'ba'), 'ba')
    print(get_score('abc', 'cba'), 'cBa')
    print(get_score('abc', 'def'), '---')
    print(get_score('aa', 'ba'), '-A')
    print(get_score('ab', 'aa'), 'A-')

