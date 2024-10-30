"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Users see a dashed word, trying to correctly figure the un-dashed word out by inputting one character each round.
    """
    ans = ''
    left = N_TURNS
    r = random_word()
    for j in range(len(r)):  # -------
        ans += '-'

    print('The word looks like: ' + str(ans))
    print('You have ' + str(left) + ' wrong guesses left.')

    while not ans.isalpha():
        input_ch = (input('Your guess: '))
        input_ch = input_ch.upper()
        if input_ch.isalpha():
            if not input_ch in r:
                left -= 1  # wrong ans: 扣次數
                print("There is no " + str(input_ch) + "'s in the word.")
                print('The word looks like: ' + str(ans))
                print('You have ' + str(left) + ' wrong guesses left.')
            else:
                all_ans = ''  # 存
                for i in range(len(r)):
                    ch = r[i]
                    if input_ch == ch:  # input_ch敲到r的房門 停在那 換
                        all_ans += ch
                    else:
                        all_ans += ans[i]  # 其他房門用‘-’取代
                ans = all_ans  # all_ans儲存前幾turn的hint
                print('You are correct!')
                print('The word looks like: ' + str(ans))
                print('You have ' + str(left) + ' wrong guesses left.')
        else:
            print('Illegal format!')
    if ans.isalpha():
        print('You win!!')
        print('The answer is: '+ans)
    else:
        print('You are completely hung :(')
        print('The answer is: ' + ans)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
