import numpy as np
import random
import copy


class Tic_Tac_Board:
    BOARD_DICTIONARY = {
        0: '_',
        1: 'o',
        2: 'x'
    }

    magic_square = np.array([
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ])

    def __init__(self, board_state=None):
        self.board_state = [[0 for i in range(3)]
                            for j in range(3)]

    def board_rep(self):
        tic_tac_rep = []
        for row in self.board_state:
            tic_tac_rep.append([])
            for v, val in enumerate(row):
                tic_tac_rep[-1].append(self.BOARD_DICTIONARY[val])
        return tic_tac_rep

    def __str__(self):
        board_rep = ''
        board_list_rep = self.board_rep()
        for row in board_list_rep:
            new_row = ' '.join(row) + '\n'
            board_rep += new_row

        return board_rep

    def calculate_sum(self, player_state):
        sums = []
        temp_state = np.array(player_state, dtype=int)

        for i in range(2):
            sums.extend(np.sum(temp_state, axis=i))
        sums.append(np.trace(temp_state))
        sums.append(np.trace(np.transpose(temp_state)))

        check_sums = [s == 15 for s in sums]

        return any(check_sums)

    def play_random(self):
        print(self)

        player_state = copy.deepcopy(self.board_state)
        computer_state = copy.deepcopy(self.board_state)
        # win_state = False
        open_pos = [(i, j) for i in range(3) for j in range(3)]

        while True:
            player_move = input('Please enter position on square:\n').split()
            print(player_move)
            row, col = list(map(int, player_move))
            print(row, col)
            if (row, col) in open_pos:
                player_state[row][col] = self.magic_square[row][col]
                self.board_state[row][col] = 2
                open_pos.remove((row, col))
            else:
                print('You have chosen a wrong position')
                continue
            print(self)

            if self.calculate_sum(player_state):
                print('You won!')
                break

            c_row, c_col = random.choice(open_pos)
            computer_state[c_row][c_col] = self.magic_square[c_row][c_col]
            self.board_state[c_row][c_col] = 1
            open_pos.remove((c_row, c_col))
            print(self)

            if self.calculate_sum(computer_state):
                print('You lost!')
                break


if __name__ == '__main__':
    board1 = Tic_Tac_Board()
    # print(board1)
    # print(board1.calculate_sum(board1.board_state))
    board1.play_random()
