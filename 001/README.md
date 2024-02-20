Hello, I am somewhat of a Python novice so this solution may lack in readability and optimization.

My solution works by taking the returned clue, iterating through the word list, and removing words that cannot be correct based on the returned clue. It will then pick a random word from the remaining words to use as a new guess and repeat until the returned clue is "🟩🟩🟩🟩🟩".

The function usually takes more than 6 guesses unless it gets lucky.
