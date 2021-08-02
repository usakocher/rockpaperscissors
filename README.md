# rockpaperscissors

## Overview
This is a computer game where a single player can play against a computer in a standard game of Rock Paper Scissors

## Assumptions
The program assumes that the player already knows the rules of the game and, as of this moment, does not explain them.

## Program
The program provides two different computer opponents for the player. One is a computer that plays a completely random
decision. The other plays according to general strategy for the game.

## Strategy
#### Random Opponent
The random opponent generates a random number from zero to three and applies that number as the index position of a list of choices.
No other strategy is employed

#### Stategic Opponent
The strategic opponent takes in some extra data to evaluate before deciding on a play. It looks at the last two player desicions and the
result of the previous game to decide on a play in the following order:<br>

If the player has played the same choice the last two times, the computer will play the choice that would be beaten by the repeated choice. 
Because Naive players don’t like to repeat the same throw more than twice in a row. The counterstrategy is to choose whatever sign the doubled
sign would beat. Should your opponent throw rock and rock a second time; you would want to choose scissors on the next throw. Given that 
the opponent is unlikely to play rock again, scissors would be unbeatable. In case of paper, scissors wins; should the opponent choose scissors, it’s a tie.<br>

The second strategy is called mirroring. If you just won, play what your opponent just played, because he or she will think that you are going 
to play the same gesture again. The opponent looks at the previous play and a boolean value of if it had won the previous throw.<br>

The final strategy is the countertactic: Let’s say you played scissors and your opponent played rock. The chance that your opponent will confidently 
play rock again is now very high. What that means to you: anticipate that and play paper. In other words: play the option that wasn’t played in the previous round.<br>

Should none of those strategies take place, or should it be the first play of the game, the computer will randomly choose based on weighted choices. Statistically
rock, paper, and scissors are not thrown equally. Therefore the computer will play based on those statistics: 35.4% Rock, 35% Paper and 29.6% Scissors.<br>

## Ending
Ending the program is as simple as saying you don't want to play. The program will then compile and display your statistics. It does not keep statistics on ties,
but will display the player's overall W/L record, as well as the percentage of wins for each type of play. If a win or loss is not recorded (as in a player does not
play to a decision), then the program will tell the player that there is not enough data for statistics. If a single decision is recorded then it will
return all statistics.

## Lessons Learned
I had a lot of fun designing this program. Providing a strategy option not only increased the difficulty level, but helped reinforce OOP principles as well as
figuring out a way to employ both options with an efficient code. I look forward to projects like this in the future.
