import tkinter as tk
import numpy as np
import copy
'''
A basic application to play Tic Tac Toe, created using the python
GUI framework Tkinter. Running this python code will open up a small
window and start playing
'''


class Tic_Tac_App(tk.Frame):
    '''
    This Tic_Tac_App class inserts a Tkinter frame object into whatever
    you pass to it, most commonly the parent Window container.
    Theoretically a frame container would alos work, if you  wanted to
    build a bigger app using this class.

    **Class Variables**
        BOARD_DICTONARY: *dictionary*
            the keys are the ints 0, 1 and 2 and the corresponding values
            are characters that show up on the app buttons according to
            the player whose turn it is, with the start of the game displaying
            empty buttons
        magic_square: *np.array, int*
            A 3 x 3 array of ints. The sums of all the rows, columns and diagonals
            add upto 15. It is used to check if any player has won, according to
            which blocks the player has clicked on

    **Attributes**
        master: *tkinter wondow/frame object*
            The master tkinter container that holds the Tic Tac App frame
            that is being created
    '''
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
        self.exit_button = self.exit()

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
        # print(i, j)
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
            # print(self.player1)
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

    def exit(self):
        quit = tk.Button(self, command=self.master.destroy)
        quit.pack(side='bottom')
        return Tic_Tac_App2()

class Tic_Tac_App2(tk.Frame):
    '''
    This Tic_Tac_App class inserts a Tkinter frame object into whatever
    you pass to it, most commonly the parent Window container.
    Theoretically a frame container would alos work, if you  wanted to
    build a bigger app using this class.

    **Class Variables**
        BOARD_DICTONARY: *dictionary*
            the keys are the ints 0, 1 and 2 and the corresponding values
            are characters that show up on the app buttons according to
            the player whose turn it is, with the start of the game displaying
            empty buttons
        magic_square: *np.array, int*
            A 3 x 3 array of ints. The sums of all the rows, columns and diagonals
            add upto 15. It is used to check if any player has won, according to
            which blocks the player has clicked on

    **Attributes**
        master: *tkinter wondow/frame object*
            The master tkinter container that holds the Tic Tac App frame
            that is being created
    '''
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
        # print(i, j)
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
            # print(self.player1)
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
