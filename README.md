# AI-Chess-Bot-2.0

This is my 2nd attempt at a minimax chess intelligence (you can see the first [here](https://github.com/DanielT504/AI-Chess-Bot)), this time without many of the bells and whistles of my last program, which I believe may have hindered its computational efficiency. I've also added a grade of ideality for the board position of each type of piece, to incentivize stronger placements. I plan to reintroduce the more advanced techniques one by one more carefully than before.

Currently acts based on positional/structural incentives, capture potential, mobility, and material balance. It can sometimes get stuck in loops of jiggling the rook back and forth to remain in a neutral state. The alpha-beta pruning helps with the computation time, but anything longer than a depth of 3 will take several minutes per move.

![chess-bot](https://github.com/DanielT504/AI-Chess-Bot-2.0/assets/62156098/e632f10e-0483-4998-8e0d-6da8adb1aae8) 

*result of a facilitated game between my AI and Chess.com's starter player

![image](https://github.com/DanielT504/AI-Chess-Bot-2.0/assets/62156098/f7c352ae-2c97-4add-9caf-acb560404329)

TODO:

*Evaluation of:  king safety, incentivize pawn chains

Transposition table

Iterative deepening

Quiescence search

Aspiration window search

Move ordering

Late move reduction

end game specific evaluation

user pawn promotion, piece icons
