from urllib.request import urlopen
from random import choice
import random

WORD_LIST_URL = "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"


with urlopen(WORD_LIST_URL) as f:
    WORDS = f.read().decode("utf-8").upper().splitlines()


class Wordle:
    def __init__(self, word: str | None = None) -> None:
        self._secret = word or choice(WORDS)
        self.clues: list[str] = []

    def guess(self, word: str) -> str:
        word = word.upper()
        assert len(word) == 5, "Word must be 5 letters long"

        clue: str = ["⬜"] * 5

        for i, letter in enumerate(word):
            if letter in self._secret:
                if letter == self._secret[i]:
                    clue[i] = "🟩"
                else:
                    clue[i] = "🟨"

        self.clues.append("".join(clue))

        return self.clues[-1]
    
def solve_wordle(wordle: Wordle, initial_guess: str) -> str:
    tlist = tuple(WORDS)
    hint = wordle.guess(initial_guess)
    print("guessing   " + initial_guess)
    print(hint + "   hint returned")
    while hint != "🟩🟩🟩🟩🟩":
        for x in tlist:
            for i in range(5):
                if hint[i] == "⬜" and initial_guess[i] in x:
                    WORDS.remove(x)
                    break
                elif hint[i] == "🟩" and initial_guess[i] != x[i]:
                    WORDS.remove(x)
                    break
                elif hint[i] == "🟨" and initial_guess[i] not in x:
                    WORDS.remove(x)
                    break
                elif hint[i] == "🟨" and initial_guess[i] == x[i]:
                    WORDS.remove(x)
                    break
        tlist = tuple(WORDS)
        initial_guess = random.choice(WORDS)
        hint = wordle.guess(initial_guess)
        print("guessing   " + initial_guess)
        print(hint + "   hint returned")
    return initial_guess
   
    
    # write your code here 👆👆



if __name__ == "__main__":
    game = Wordle()
    solution = solve_wordle(game, "SLATE")
    print(f"The solution is {solution}")
    

    