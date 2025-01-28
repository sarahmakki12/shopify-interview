import random

class Game:
    def __init__(self, dictionary_path, lives = 5):
        self.dictionary = Dictionary(dictionary_path)
        self.target = self.dictionary.getTarget()
        self.lives = lives

    def guess(self, word):
        if self.lives <= 0:
            return 'game over'
        
        if not self.dictionary.checkWord(word):
            return 'r'
        elif word == self.target:
            return 'a'
        else:
            hint = self.getHint(word)
            self.lives -= 1
            return hint
        
    def getHint(self, word):
        hint = ''
        for idx, letter in enumerate(word):
            targetLetter = self.target[idx]
            if letter == targetLetter:
                hint += '1'
            else:
                if letter in self.target:
                    hint += '0'
                else:
                    hint += '-'
        return hint
    
    def hasLives(self):
        return self.lives > 0

class Dictionary:
    def __init__(self, dictionary_path):
        self.dictionary = set()
        with open(dictionary_path, 'r') as file:
            for line in file:
                self.dictionary.add(line.strip())

    def getTarget(self):
        return random.choice(tuple(self.dictionary))
    
    def checkWord(self, word):
        return word in self.dictionary