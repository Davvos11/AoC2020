from time import time

tests = [[0, 3, 6], [1, 3, 2], [2, 1, 3], [1, 2, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
test_answers = [436, 1, 10, 27, 78, 438, 1836]
input15 = [0, 1, 4, 13, 15, 12, 16]


class MemoryGame:
    def __init__(self, starting_numbers: [int]):
        self.last_spoken = []
        self.starting_numbers = starting_numbers
        self.index = 0
        self.last_num = starting_numbers[-1]

    def play(self, rounds: int):
        self.last_spoken = [[None, None] for i in range(rounds)]
        for i, num in enumerate(self.starting_numbers):
            self.last_spoken[num][1] = i
            self.index += 1

        # Then, each turn consists of considering the most recently spoken number:
        while self.index < rounds:
            try:
                last_num_history = self.last_spoken[self.last_num]

                # If that was the first time the number has been spoken, the current player says 0.
                if last_num_history[0] is None:
                    self.last_num = 0
                # Otherwise, the number had been spoken before;
                # the current player announces how many turns apart the number is from when it was previously spoken.
                else:
                    self.last_num = last_num_history[1] - last_num_history[0]

            except KeyError:
                # If this is the first time the number has been spoken, the current player says 0.
                self.last_num = 0

            try:
                current_num_history = self.last_spoken[self.last_num]
                current_num_history[0] = current_num_history[1]
                current_num_history[1] = self.index
            except KeyError:
                self.last_spoken[self.last_num] = [None, self.index]

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
