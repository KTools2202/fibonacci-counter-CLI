import tkinter as tk
from tkinter import messagebox
import pyperclip
from library.fibonacciCounter import fibonacciCounter

fib = fibonacciCounter()


def calculate():
    count = count_entry.get()
    display = display_var.get()
    if display not in ["all", "position"]:
        messagebox.showerror("Error",
                             "Invalid display argument!",
                             "Valid arguments: all, position.")
        return

    result = fib.counter(int(count), str(display))

    # Display result in the GUI
    result_text.delete(1.0, tk.END)  # Clear previous result

    if print_var.get():
        result_text.insert(tk.END, result)  # Insert new result
    if copy_var.get():
        pyperclip.copy(result)
        result_text.insert(tk.END, "\nCopied result to clipboard.")
        messagebox.showinfo("Info", "Result copied to clipboard.")
    if not print_var.get() and not copy_var.get():
        messagebox.showwarning("Error",
                               "Choose a way to output the result.")


# GUI setup
root = tk.Tk()
root.title("Fibonacci Counter")

tk.Label(root, text="Count:").grid(row=0, column=0)
count_entry = tk.Entry(root)
count_entry.grid(row=0, column=1)

tk.Label(root, text="Display:").grid(row=1, column=0)
display_var = tk.StringVar(value="all")
tk.OptionMenu(root, display_var, "all", "position").grid(row=1, column=1)

print_var = tk.BooleanVar()
tk.Checkbutton(root, text="Print Result",
               variable=print_var).grid(row=2, columnspan=2)

copy_var = tk.BooleanVar()
tk.Checkbutton(root, text="Copy Result", variable=copy_var).grid(row=3,
                                                                 columnspan=2)

frame = tk.Frame(root)
frame.grid(row=5, columnspan=2)

# Text widget to display the result with line wrapping
result_text = tk.Text(root, height=10, width=40)
result_text.grid(row=5, columnspan=2)
result_text.config(wrap=tk.WORD)  # Enable word wrapping

tk.Button(root, text="Calculate", command=calculate).grid(row=4, columnspan=2)

root.mainloop()
