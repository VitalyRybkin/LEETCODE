"""
A phrase is a palindrome if, after converting all
uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
#s = "A man, a plan, a canal: Panama"
s = "A man, a plan, a cameo, Zena, Bird, Mocha, Prowel, a rave, Uganda, Wait, a lobola, Argo, Goto, Koser, Ihab, Udall, a revocation, Ebarta, Muscat, eyes, Rehm, a cession, Udella, E-boat, OAS, a mirage, IPBM, a caress, Etam, FCA, a mica, Ojai, Lebowa, Yaeger, a barge, Rab, Alsatian, a mod, Adv, a rps, Ileane, Valeta, Grenada, Hetty, Fayme, REME, HCM, Tsan, Owena, Tamar, Yompur, Isa, Nil, Lorrin, Riksdag, Mona, Ronn, O'Conner, Kirk, an okay, Nafl"

import time

def isPalindrome(s: str) -> bool:
    res = ''
    s = s.replace(' ', '')
    s = s.replace(',', '')
    s = s.replace(':', '')
    for _ in s:
        if _.isalnum() :
            res += _.lower()

    if not res == res[::-1]:
        return False

    return True

st = time.time()
print(isPalindrome(s))
et = time.time()
print(et - st)
