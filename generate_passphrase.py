#!/usr/bin/env python

"""
Memorable password generator
based on: https://github.com/wheelybird/ldap-user-manager/blob/master/www/js/generate_passphrase.js
"""

import wordlist # list of words
import secrets, random, math

def generatePassword(numberOfWords: int, seperator: str):
  # numberOfWords - number of words (int)
  # separator - character (str)

  # wordlist.wordlist - list of words

  # Cryptographically generated random numbers
  lst = list(map(str, [secrets.randbits(32) for i in range(numberOfWords)]))

  # Empty list to be filled with wordlist
  generatedPassword = []

  integerIndex = getRandomInt(4)
  integerValue = getRandomInt(99)
  uppercaseIndex = getRandomInt(4)

  while uppercaseIndex == integerIndex:
    uppercaseIndex = getRandomInt(4)

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


def getRandomInt(maxVal):
  return math.floor(random.random() * math.floor(maxVal));

#print(generatePassword(4, "-"))
