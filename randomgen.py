#! /usr/bin/env python3
import string
import random

class randomgen:
    def get_random_word(self,wordLen):
        word = ''
        for i in range(wordLen):
            word+=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
        return word


    def str(self):
        wordLen = random.randint(5, 15)
        word = self.get_random_word(wordLen)
        return word

    def int(self):
        return random.randint(5,100)


r = randomgen()
print(r.str())
print(r.int())
