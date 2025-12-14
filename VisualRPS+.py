import random
import tkinter as tk

root = tk.Tk()
root.title("Rock Paper Scissors Lizard Spock")
root.geometry("1000x700")
imgBG = tk.PhotoImage(file="BG.png")
imgR = tk.PhotoImage(file="Rnew.png")
imgP = tk.PhotoImage(file="P.png")
imgS = tk.PhotoImage(file="Snew.png")
imgSp = tk.PhotoImage(file="Spnew.png")
imgL = tk.PhotoImage(file="Lnew.png")
player_score = 0
computer_score = 0
bg_label = tk.Label(root, image=imgBG)
bg_label.place(y=0, x=0, relwidth=1, relheight=1)
l1 = tk.Label(root, text="Rock Paper Scissors Lizard Spock", font=("Georgia", 20), fg="darkslategray", bg="white")
l1.pack()
win = tk.Label(root, text="Make your choice!", font=("Comic Sans MS", 14), fg="darkcyan", bg="white")
win.pack()
score = tk.Label(root, text="Player: 0 | Computer: 0", font=("Comic Sans MS", 14), fg="lightseagreen", bg="white")
score.pack()
def game(player_choice):
    global player_score
    global computer_score
    computer_choice = random.choice(["rock", "paper", "scissors", "lizard", "spock"])
def game(player_choice):
    global player_score
    global computer_score
    computer_choice = random.choice(
        ["rock", "paper", "scissors", "lizard", "spock"]
    )
    if player_choice == computer_choice:
        result = "Both Win"
    elif (
        (player_choice == "rock" and computer_choice in ["scissors", "lizard"]) or
        (player_choice == "paper" and computer_choice in ["rock", "spock"]) or
        (player_choice == "scissors" and computer_choice in ["paper", "lizard"]) or
        (player_choice == "lizard" and computer_choice in ["paper", "spock"]) or
        (player_choice == "spock" and computer_choice in ["rock", "scissors"])
):
        result = "Player Wins"
        player_score += 1
    else:
        result = "Computer Wins"
        computer_score += 1
    win.config(text=f"Player: {player_choice.upper()} | Computer: {computer_choice.upper()}\n{result}")
    score.config(text=f"Player: {player_score} | Computer: {computer_score}")
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, image=imgR, command=lambda: game("rock")).grid(row=0, column=0)
tk.Button(frame, image=imgP, command=lambda: game("paper")).grid(row=0, column=1)
tk.Button(frame, image=imgS, command=lambda: game("scissors")).grid(row=0, column=2)
tk.Button(frame, image=imgL, command=lambda: game("lizard")).grid(row=1, column=0, padx=5)
tk.Button(frame, image=imgSp, command=lambda: game("spock")).grid(row=1, column=1, padx=5)
root.mainloop()