import tkinter as tk

def start_game(mode):
    global board, turn
    board = [" " for i in range(9)]
    turn = "X"
    for i in range(9):
        b[i].config(text=" ", state="normal")
    if mode == "single":
        tk.messagebox.showinfo("Info", "You are playing against the computer.")
    else:
        tk.messagebox.showinfo("Info", "You are playing against another player.")

def click(idx):
    global board, turn
    if board[idx] == " ":
        board[idx] = "X" if turn == "X" else "O"
        b[idx].config(text=board[idx], fg=("red" if turn == "X" else "green"), state="disabled")
        check_game()
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

def check_game():
    global board
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != " ":
            win(board[i])
            return
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != " ":
            win(board[i])
            return
    if board[0] == board[4] == board[8] and board[0] != " ":
        win(board[0])
        return
    if board[2] == board[4] == board[6] and board[2] != " ":
        win(board[2])
        return
    if " " not in board:
        draw()

def win(player):
    tk.messagebox.showinfo("Congratulations!", f"{player} wins!")
    root.destroy()

def draw():
    tk.messagebox.showinfo("Draw!", "It's a draw!")
    root.destroy()

root = tk.Tk()
root.title("Tic Tac Toe")

board = [" " for i in range(9)]
turn = "X"

b = [0 for i in range(9)]

for i in range(9):
    b[i] = tk.Button(root, text=" ", font=("Helvetica", 20), width=4, height=2, command=lambda idx=i: click(idx))
    b[i].grid(row=i // 3, column=i % 3)

menubar = tk.Menu(root)
game_menu = tk.Menu(menubar, tearoff=0)
game_menu.add_command(label="2 Players", command=lambda: start_game("multi"))
game_menu.add_command(label="Against PC", command=lambda: start_game("single"))
menubar.add_cascade(label="Game", menu=game_menu)
root.config(menu=menubar)
root.mainloop()
