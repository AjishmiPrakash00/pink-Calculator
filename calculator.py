import tkinter as tk

# Create the window
window = tk.Tk()
window.title("Pink Calculator")
window.configure(bg="#ffe6f0")  # Light pink background

# Entry box (input/output)
entry = tk.Entry(window, width=20, font=("Arial", 18), borderwidth=2, relief="solid", bg="#fff0f5", fg="#99004d")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to insert number/operator
def button_click(value):
    entry.insert(tk.END, value)

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# Function to calculate result
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Common pastel button style
button_style = {
    "width": 5,
    "height": 2,
    "font": ("Arial", 14),
    "bg": "#ffd6e7",        # Soft pink button
    "fg": "#4d0039",        # Dark text
    "activebackground": "#ffccdd"  # Pressed color
}

# Layout of buttons (text, row, column)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create the buttons
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(window, text=text, command=calculate, **button_style).grid(row=row, column=col)
    else:
        tk.Button(window, text=text, command=lambda t=text: button_click(t), **button_style).grid(row=row, column=col)

# Clear button (full width)
tk.Button(window, text="C", command=clear, width=22, height=2, font=("Arial", 14),
          bg="#ffb3cc", fg="#660033", activebackground="#ffa6c9").grid(row=5, column=0, columnspan=4, pady=5)

# Run the app
window.mainloop()
