import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'

        # Create buttons
        self.buttons = [[None, None, None] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text='', font=('normal', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.buttons[row][col]['text'] == '':
            self.buttons[row][col]['text'] = self.current_player

            # Check for a winner
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if all(self.buttons[i][j]['text'] == self.current_player for j in range(3)) or \
               all(self.buttons[j][i]['text'] == self.current_player for j in range(3)):
                return True

        if all(self.buttons[i][i]['text'] == self.current_player for i in range(3)) or \
           all(self.buttons[i][2 - i]['text'] == self.current_player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(self.buttons[i][j]['text'] != '' for i in range(3) for j in range(3))

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
        self.current_player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
