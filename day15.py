from time import time

tests = [[0, 3, 6], [1, 3, 2], [2, 1, 3], [1, 2, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
test_answers = [436, 1, 10, 27, 78, 438, 1836]
input15 = [0, 1, 4, 13, 15, 12, 16]


class MemoryGame:
    def __init__(self, starting_numbers: [int]):
        self.last_spoken = {num: [i] for i, num in enumerate(starting_numbers)}
        self.index = len(self.last_spoken)
        self.last_num = starting_numbers[-1]

    def play(self, rounds: int):
        # Then, each turn consists of considering the most recently spoken number:
        while self.index < rounds:
            # If that was the first time the number has been spoken, the current player says 0.
            if self.last_spoken[self.last_num] is None or len(self.last_spoken[self.last_num]) <= 1:
                self.last_num = 0
            # Otherwise, the number had been spoken before;
            # the current player announces how many turns apart the number is from when it was previously spoken.
            else:
                self.last_num = self.last_spoken[self.last_num][-1] - self.last_spoken[self.last_num][-2]

            # Update dictionaries
            if self.last_num in self.last_spoken:
                self.last_spoken[self.last_num].append(self.index)
            else:
                self.last_spoken[self.last_num] = [self.index]

            # Update index
            self.index += 1


if __name__ == '__main__':
    print("Puzzle 1 tests:")
    for i, test in enumerate(tests):
        game = MemoryGame(test)
        game.play(2020)
        print(f"   {test}: {game.last_num}, {game.last_num == test_answers[i]}")

    t1 = time()
    game = MemoryGame(input15)
    game.play(2020)
    print(f"Puzzle 1: {game.last_num}")
    print(f"   Time: {time() - t1} seconds\n")

    t1 = time()
    game = MemoryGame(input15)
    game.play(30000000)
    print(f"Puzzle 2: {game.last_num}")
    print(f"   Time: {time() - t1} seconds")
