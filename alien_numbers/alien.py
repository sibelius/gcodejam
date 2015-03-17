#!/usr/bin/env python3
"""
Convert a number from one base to another

Input:
    alien_number source_language target_language

Output:
    Case #{}: number_in_target_language

"""

def convert(num, s, t):
    sb = len(s)
    st = len(t)

    return listToLang(
        tenToK(
            kToTen(
                langToList(
                    num, s),
                sb),
            st),
        t)

def langToList(_str, lang):
    return [lang.find(s) for s in _str]

def listToLang(lst, lang):
    return ''.join(lang[l] for l in lst)

def tenToK(number, base):
    res = []
    while number > 0:
        rest = number % base
        number = number // base
        res.append(rest)
    res.reverse()

    return res

def kToTen(number, base):
    n = len(number)
    return sum([number[i] * (base ** (n-i-1)) for i in range(n)])

def process(case):
    num, source, target = input().split()

    print('Case #{}: {}'.format(case, convert(num, source, target)))

if __name__ == '__main__':
    n = int(input())

    for i in range(1,n+1):
        process(i)
