import tkinter as tk
from tkinter import messagebox

def update_output(number):
    output_text.insert(tk.END, number)

def display_numbers():
    displayed_text = output_text.get("1.0", tk.END)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")

def equalsPress():
    try:
        displayed_text = output_text.get("1.0", tk.END).strip()
        # Evaluate the expression
        result = str(eval(displayed_text))
        # Clear the output box and display the result
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Output Section
output_text = tk.Text(root, height=5, width=50)
output_text.grid(row=0, column=0, columnspan=3, pady=5)

# Buttons
button1 = tk.Button(root, text="1", command=lambda: [update_output("1"), display_numbers()])
button1.grid(row=1, column=0, padx=5, pady=5)

button2 = tk.Button(root, text="2", command=lambda: [update_output("2"), display_numbers()])
button2.grid(row=1, column=1, padx=5, pady=5)

button3 = tk.Button(root, text="3", command=lambda: [update_output("3"), display_numbers()])
button3.grid(row=1, column=2, padx=5, pady=5)

button4 = tk.Button(root, text="4", command=lambda: [update_output("4"), display_numbers()])
button4.grid(row=2, column=0, padx=5, pady=5)

button5 = tk.Button(root, text="5", command=lambda: [update_output("5"), display_numbers()])
button5.grid(row=2, column=1, padx=5, pady=5)

button6 = tk.Button(root, text="6", command=lambda: [update_output("6"), display_numbers()])
button6.grid(row=2, column=2, padx=5, pady=5)

button7 = tk.Button(root, text="7", command=lambda: [update_output("7"), display_numbers()])
button7.grid(row=3, column=0, padx=5, pady=5)

button8 = tk.Button(root, text="8", command=lambda: [update_output("8"), display_numbers()])
button8.grid(row=3, column=1, padx=5, pady=5)

button9 = tk.Button(root, text="9", command=lambda: [update_output("9"), display_numbers()])
button9.grid(row=3, column=2, padx=5, pady=5)

button0 = tk.Button(root, text="0", command=lambda: [update_output("0"), display_numbers()])
button0.grid(row=4, column=0, padx=5, pady=5)

buttonPlus = tk.Button(root, text="+", command=lambda: [update_output("+"), display_numbers()])
buttonPlus.grid(row=4, column=1, padx=5, pady=5)

buttonMinus = tk.Button(root, text="-", command=lambda: [update_output("-"), display_numbers()])
buttonMinus.grid(row=4, column=2, padx=5, pady=5)

buttonMultiply = tk.Button(root, text="*", command=lambda: [update_output("*"), display_numbers()])
buttonMultiply.grid(row=5, column=0, padx=5, pady=5)

buttonDivide = tk.Button(root, text="/", command=lambda: [update_output("/"), display_numbers()])
buttonDivide.grid(row=5, column=1, padx=5, pady=5)

buttonEquals = tk.Button(root, text="=", command=equalsPress)
buttonEquals.grid(row=5, column=2, padx=5, pady=5)

root.mainloop()
