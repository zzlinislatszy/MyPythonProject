"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""

# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Users will be asked to input a number to produce shifted ALPHABET as the cipher table. After that, any strings typed
    in will be encrypted.
    """
    num = int(input('Secret number: '))
    og = input("What's the ciphered string? ")
    new_og = og.upper()
    alpha = new_alpha(num)
    new = ''
    for i in range(len(new_og)):
        if not new_og[i].isalpha():
            # 建立邊界條件，如非字母，直接帶入og字元
            new += new_og[i]
        else:
            index = alpha.find(new_og[i])
            new += ALPHABET[index]
    print('The deciphered string is: '+str(new))


def new_alpha(num):
    # compose a new alphabet table
    alpha = ''
    alpha = ALPHABET[26-num:]
    alpha += ALPHABET[:26-num]
    return alpha







# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
