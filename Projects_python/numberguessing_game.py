import tkinter as tk
from tkinter import messagebox
import random

def check_guess():
    try:
        global attempts
        guess = int(guess_entry.get())
        if 1 <= guess <= 100:
            attempts += 1
            if guess == secret_number:
                messagebox.showinfo("Congratulations!", f"Correct! You guessed the number in {attempts} attempts.")
                reset_game()
            elif guess < secret_number:
                result_label.config(text="Too low! Try a higher number.")
            else:
                result_label.config(text="Too high! Try a lower number.")
            guess_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 100.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="")
    guess_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Number Guessing Game")

secret_number = random.randint(1, 100)
attempts = 0

title_label = tk.Label(root, text="Guess the Number (1-100)", font=("Arial", 18))
title_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Arial", 14))
guess_entry.pack()

submit_button = tk.Button(root, text="Submit Guess", command=check_guess, font=("Arial", 12))
submit_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", command=reset_game, font=("Arial", 12))
reset_button.pack(pady=5)

root.mainloop()
