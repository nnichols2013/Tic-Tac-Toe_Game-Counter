How many possible games of Tic Tac Toe can be played?

Some people use naive solutions. For example, the minimum number of turns required to win is 5, and the maximum is 9. So the range of conceivable games would be 5! + 6! + ... + 9!
This is incorrect partly because it doesn't account for the fact that finished games should terminate and return.

So the best and only way to accurately count them is by playing every game.
This simple python program enumerates every possible game with recursion.

The answer is 209088.
