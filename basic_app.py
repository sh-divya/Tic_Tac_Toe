import tkinter as tk
import numpy as np
import copy


class Tic_Tac_App(tk.Frame):
    BOARD_DICTIONARY = {
        0: '',
        1: 'o',
        2: 'x'
    }

    magic_square = np.array([
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ])

    def __init__(self, master=None):
        super().__init__(master, width=500, height=500, relief=tk.RIDGE)
        self.master = master
        self.master.title('Tic-Tac-Toe')
        self.pack(padx=10, pady=10)
        self.player1, self.player2 = self.reset()
        self.board_buttons = [[] for _ in range(3)]
        self.current_player = None
        self.label_text = 'Start playing!'
        self.label = self.create_grid()

    def create_grid(self):

        for i in range(3):
            for j in range(3):
                curr_button = tk.Button(self, relief=tk.GROOVE,
                                        padx=3, width=3,
                                        font=('arial', 30, 'bold'),
                                        command=lambda row=i, col=j:
                                        self.switch(row, col))
                curr_button['text'] = Tic_Tac_App.BOARD_DICTIONARY[0]
                curr_button['background'] = 'white'
                curr_button.grid(row=i, column=j)
                self.board_buttons[i].append(curr_button)

        label = tk.Label(self.master, text=self.label_text,
                         font=('arial', 20, 'bold'))
        label.pack(side='bottom')

        return label

    def reset(self):
        empty_board = [[0 for i in range(3)]
                       for j in range(3)]
        return (copy.deepcopy(empty_board),
                copy.deepcopy(empty_board))

    def switch(self, i, j):
        print(i, j)
        clicked_button = self.board_buttons[i][j]
        if self.current_player is None:
            self.current_player = 1

        clicked_button['text'] = str(Tic_Tac_App.BOARD_DICTIONARY[self.current_player + 1])

        if not self.current_player:
            self.player2[i][j] = Tic_Tac_App.magic_square[i][j]
            if self.calculate_sum(self.player2):
                self.label['text'] = 'o Won!'
                self.master.destroy
            self.current_player = 1
        else:
            print(self.player1)
            self.player1[i][j] = Tic_Tac_App.magic_square[i][j]
            if self.calculate_sum(self.player1):
                self.label['text'] = 'x Won!'
                self.master.destroy
            self.current_player = 0

    def calculate_sum(self, player_state):
        sums = []
        temp_state = np.array(player_state, dtype=int)

        for i in range(2):
            sums.extend(np.sum(temp_state, axis=i))
        sums.append(np.trace(temp_state))
        sums.append(np.trace(np.transpose(temp_state)))

        check_sums = [s == 15 for s in sums]

        return any(check_sums)


if __name__ == '__main__':
    root = tk.Tk()
    ttt = Tic_Tac_App(root)
    root.mainloop()
