#! /usr/bin/env python3
import string
import random

class RandomGen:
    def get_random_word(self,wordLen):
        word = ''
        for i in range(wordLen):
            word+=random.choice(string.ascii_letters + string.digits)
        return word


    def string(self):
        wordLen = random.randint(5, 15)
        word = self.get_random_word(wordLen)
        return word

    def integer(self):
        return str(random.randint(5,100))
