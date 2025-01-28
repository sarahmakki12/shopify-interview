import random

class Game:
    def __init__(self, dictionary_path):
        self.dictionary = Dictionary(dictionary_path)
        self.target = self.dictionary.getTarget()

    def guess(self, word):
        if not self.dictionary.checkWord(word):
            return 'r'
        elif word == self.target:
            return 'a'
        else:
            return self.getHint(word)
        
    def getHint(self, word):
        return ''

class Dictionary:
    def __init__(self, dictionary_path):
        self.dictionary = {}
        with open(dictionary_path, 'r') as file:
            for line in file:
                self.dictionary.add(line.strip())

    def getTarget(self):
        return random.choice(tuple(self.dictionary))
    
    def checkWord(self, word):
        return word in self.dictionary