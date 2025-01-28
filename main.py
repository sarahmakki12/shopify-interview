from game import Game

def main():
    game = Game('sample-dictionary/a2b036e7ee0777d630571e63ebbeacc3-78b2d0a5e9e371989688ecb27b25ea0c14252ef3/sample_dictionary.txt')
    print(game.target)

    while game.hasLives():
        guess = input('Enter your guess: ')
        hint = game.guess(guess)
        if hint == 'r':
            print('Invalid word, guess again')
        elif hint == 'a':
            print('Correct! Game won')
            break
        else:
            print('Hint: ', hint)

    if game.hasLives():
        print('Game won')
    else:
        print('Game over')

main()