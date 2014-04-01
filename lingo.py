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
            

