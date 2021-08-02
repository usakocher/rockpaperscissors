import random


class Player:
    def __init__(self):
        self.wins = {'Rock': 0, 'Paper': 0, 'Scissors':0}
        self.losses = {'Rock': 0, 'Paper': 0, 'Scissors':0}

    def printStats(self):
        self.totalWins = self.wins['Rock'] + self.wins['Paper'] + self.wins['Scissors']
        self.totalLosses = self.losses['Rock'] + self.losses['Paper'] + self.losses['Scissors']
        if self.totalWins != 0 or self.totalLosses != 0:
            print(f'Your overall record was {self.totalWins} - {self.totalLosses}')
            sharesRock = self.wins['Rock']/(self.totalWins + self.totalLosses)
            sharesPaper = self.wins['Paper']/(self.totalWins + self.totalLosses)
            sharesScissors = self.wins['Scissors']/(self.totalWins + self.totalLosses)
            print('You were successful ' + "{:.2%}".format(sharesRock) + ' for Rock')
            print('You were successful ' + "{:.2%}".format(sharesPaper) + ' for Paper')
            print('You were successful ' + "{:.2%}".format(sharesScissors) + ' for Scissors')
            return
        else:
            print('Not enough data collected to return statistics.')


class RandomOpponent:
    def __init__(self):
        self.choices = ['Rock', 'Paper', 'Scissors']
        self.previous = {'Last': '0', 'secondLast': '1'}
        self.play = ['blank']

    def computerPlay(self):
        return self.choices[random.randint(0,2)]


class StratOpponent:
    def __init__(self):
        self.choices = ['Rock', 'Paper', 'Scissors']
        self.previous = {'Last': '0', 'secondLast': '1'}
        self.play = ['blank']

    def computerPlay(self):
        win = False
        if self.previous['Last'] == 'Rock' and self.previous['secondLast'] == 'Rock':
            return 'Scissors'
        elif self.previous['Last'] == 'Paper' and self.previous['secondLast'] == 'Paper':
            return 'Rock'
        elif self.previous['Last'] == 'Scissors' and self.previous['secondLast'] == 'Scissors':
            return 'Paper'
        elif self.previous['Last'] == 'Rock' and win == True:
            return 'Rock'
        elif self.previous['Last'] == 'Paper' and win == True:
            return 'Paper'
        elif self.previous['Last'] == 'Scissors' and win == True:
            return 'Scissors'
        elif self.previous['Last'] == 'Rock' and self.play == 'Paper':
            return 'Scissors'
        elif self.previous['Last'] == 'Paper' and self.play == 'Scissors':
            return 'Rock'
        elif self.previous['Last'] == 'Rock' and self.play == 'Scissors':
            return 'Paper'
        else:
            answer = random.choices(self.choices, weights=[35.4, 35.0, 29.6], k = 1)
            return answer[0]

class Game:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def validate(self):
        while True:
            choice = input('Please make a choice: rock, paper or scissors ')
            if choice.lower() == 'rock' or choice.lower() == 'paper' or choice.lower() == 'scissors':
                return choice.title()
            else:
                print('Please make a valid selection.')

    def run(self):
        while True:
            response = input('Do you want to play rock-paper-scissors? (y/n) ')
            if response.lower() == 'y':
                choice = self.validate()
                enemy = opponent.computerPlay()
                opponent.play = enemy
                if choice.title() == enemy:
                    print('Game Tied')
                elif choice.lower() == 'rock' and enemy == 'Scissors':
                    print('You Win')
                    player.wins['Rock'] += 1
                    opponent.win = False
                    opponent.previous['secondLast'] = opponent.previous['Last']
                    opponent.previous['Last'] = choice.title()
                elif choice.lower() == 'paper' and enemy == 'Rock':
                    print('You Win')
                    player.wins['Paper'] += 1
                    opponent.win = False
                    opponent.previous['secondLast'] = opponent.previous['Last']
                    opponent.previous['Last'] = choice.title()
                elif choice.lower() == 'scissors' and enemy == 'Paper':
                    print('You Win')
                    player.wins['Scissors'] += 1
                    opponent.win = False
                    opponent.previous['secondLast'] = opponent.previous['Last']
                    opponent.previous['Last'] = choice.title()
                elif choice.lower() == 'rock' and enemy == 'Paper':
                    print('You Lose')
                    player.losses['Rock'] += 1
                    opponent.win = True
                    opponent.previous['secondLast'] = opponent.previous['Last']
                    opponent.previous['Last'] = choice.title()
                elif choice.lower() == 'paper' and enemy == 'Scissors':
                    print('You Lose')
                    player.losses['Paper'] += 1
                    opponent.win = True
                    opponent.previous['secondLast'] = opponent.previous['Last']
                    opponent.previous['Last'] = choice.title()
                elif choice.lower() == 'scissors' and enemy == 'Rock':
                    print('You Lose')
                    player.losses['Scissors'] += 1
                    opponent.win = True
                    opponent.previous['secondLast'] = opponent.previous['Last']
                    opponent.previous['Last'] = choice.title()
            elif response.lower() == 'n':
                player.printStats()
                break
            else:
                print('Sorry, choose yes or no.')

print('Welcome to Rock, Paper, Scissors!')
player = Player()
while True:
    challenge = input('Would you like to play a random opponent or one that uses strategy? (r/s) ')
    if challenge.lower() == 'r':
        opponent = RandomOpponent()
        break
    elif challenge.lower() == 's':
        opponent = StratOpponent()
        break
    else:
        print('Please select an opponent.')
game = Game(player, opponent)
game.run()