"""
File: complement.py
Name: zzz.
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
The program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    TODO:
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(s):
    """
    : param old_s: str, the old string containing digits and ch
    : return new_s:  str, the string replacing '1' to 'A', '2' to 'B', '3' to 'C'
    """
    ans = ''
    if len(s) == 0:
        # ''will execute 0 time in for-loop
        ans = 'DNA strand is missing.'
    for i in range(len(s)):
        ch = s[i]
        if ch == 'A':
            ans = ans + 'T'
        if ch == 'T':
            ans = ans + 'A'
        if ch == 'C':
            ans = ans + 'G'
        if ch == 'G':
            ans = ans + 'C'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
