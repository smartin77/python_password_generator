#!/usr/bin/env python

"""
Memorable password generator
based on: https://github.com/wheelybird/ldap-user-manager/blob/master/www/js/generate_passphrase.js
"""

import wordlist # list of words
import secrets, random, math

def generate_password(numberOfWords: int, seperator: str):
  # function returns passphrase string
  # numberOfWords - number of words (int)
  # separator - character (str)

  # wordlist.wordlist - list of words

  # Cryptographically generated random numbers
  lst = list(map(str, [secrets.randbits(32) for i in range(numberOfWords)]))

  # Empty list to be filled with wordlist
  generatedPassword = []

  integerIndex = get_random_int(4)
  integerValue = get_random_int(99)
  uppercaseIndex = get_random_int(4)

  while uppercaseIndex == integerIndex:
    uppercaseIndex = get_random_int(4)

  i = 0
  for itm in lst:
    this_word = ""
    if (i == integerIndex ):
      this_word = integerValue;
    else:
      index = (int(itm) % 5852)
      this_word = wordlist.wordlist[index]
      if (i == uppercaseIndex):
        this_word = this_word.capitalize()

    generatedPassword.append(str(this_word))

    i += 1

  return seperator.join(generatedPassword)


def get_random_int(maxVal):
  return int(math.floor(random.random() * math.floor(maxVal)));

# usage
#print(generate_password(4, "-"))
