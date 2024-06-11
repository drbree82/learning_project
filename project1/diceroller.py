import tkinter
import random

root = tkinter.Tk()
root.title("Dice Roller")
root.geometry("400x300")

def diceRoll():
    roll = random.randint(1,6)
    labelResult.config(text=f"{roll}")

roll = 0

#Buttons
buttonRoll = tkinter.Button(root, text="Roll Die", command=diceRoll)
buttonRoll.pack(pady=5)

#display
labelResult = tkinter.Label(root, text="")
labelResult.pack(pady=5)


root.mainloop()