import tkinter as tk

# Create the main window
t_root = tk.Tk()

# Set window title
t_root.title("My Tkinter Window")

# Set window size
t_root.geometry("600x600")

# Set the background color of the window
t_root.configure(bg="black")

# Define functions for button clicks
def on_add_button_click():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_text.delete("1.0", tk.END)  # Clear previous result
        result_text.insert(tk.END, str(result))
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid numbers")

def on_multiply_button_click():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_text.delete("1.0", tk.END)  # Clear previous result
        result_text.insert(tk.END, str(result))
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid numbers")

def on_subtract_button_click():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_text.delete("1.0", tk.END)  # Clear previous result
        result_text.insert(tk.END, str(result))
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid numbers")

def on_divide_button_click():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 / num2
        result_text.delete("1.0", tk.END)  # Clear previous result
        result_text.insert(tk.END, str(result))
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid numbers")

def on_modulus_button_click():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 % num2
        result_text.delete("1.0", tk.END)  # Clear previous result
        result_text.insert(tk.END, str(result))
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid numbers")

def on_power_button_click():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 ** num2
        result_text.delete("1.0", tk.END)  # Clear previous result
        result_text.insert(tk.END, str(result))
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid numbers")

# Create Entry widgets for user input
entry1 = tk.Entry(t_root, width=10)
entry2 = tk.Entry(t_root, width=10)

# Create buttons and attach the functions to them
button_add = tk.Button(t_root, text="+", command=on_add_button_click, bg="orange")
button_multiply = tk.Button(t_root, text="*", command=on_multiply_button_click, bg="orange")
button_subtract = tk.Button(t_root, text="-", command=on_subtract_button_click, bg="orange")
button_divide = tk.Button(t_root, text="/", command=on_divide_button_click, bg="orange")
button_modulus = tk.Button(t_root, text="%", command=on_modulus_button_click, bg="orange")
button_power = tk.Button(t_root, text="**", command=on_power_button_click, bg="orange")

# Create a Text widget to display the result
result_text = tk.Text(t_root, height=1, width=20)

# Place the widgets on the window using grid layout
entry1.grid(row=0, column=0, columnspan=20, pady=50)
entry2.grid(row=0, column=2, columnspan=20, pady=50)

button_add.grid(row=1, column=0, padx=15, pady=15)
button_multiply.grid(row=1, column=1, padx=15, pady=15)
button_subtract.grid(row=1, column=2, padx=15, pady=15)
button_divide.grid(row=1, column=3, padx=15, pady=15)
button_modulus.grid(row=2, column=0, padx=15, pady=15)
button_power.grid(row=2, column=1, padx=15, pady=15)

result_text.grid(row=3, column=0, columnspan=40, pady=80)

# Run the application
t_root.mainloop()
