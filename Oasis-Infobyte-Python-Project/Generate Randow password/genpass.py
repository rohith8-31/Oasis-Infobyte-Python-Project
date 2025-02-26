import secrets
import string
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def generate_password():
    try:
        length = int(length_var.get())
        if length < 8 or length > 20:
            messagebox.showerror("Error", "Password length must be between 8 and 20 characters.")
            return
        
        use_alpha = alpha_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()
        exclude_chars = exclude_var.get()
        
        characters = ""
        if use_alpha:
            characters += string.ascii_letters
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        
        characters = ''.join(c for c in characters if c not in exclude_chars)
        
        if not characters:
            messagebox.showerror("Error", "You must select at least one character type.")
            return
        
        password = []
        if use_alpha:
            password.append(secrets.choice(string.ascii_letters))
        if use_digits:
            password.append(secrets.choice(string.digits))
        if use_symbols:
            password.append(secrets.choice(string.punctuation))
        
        remaining_length = length - len(password)
        password += [secrets.choice(characters) for _ in range(remaining_length)]
        random.shuffle(password)
        
        generated_password.set("".join(password))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(generated_password.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def choose_mode():
    mode = input("Choose mode:\n1. CLI\n2. GUI\nEnter your choice: ")
    if mode == "1":
        cli_mode()
    elif mode == "2":
        gui_mode()
    else:
        print("Invalid choice! Please enter 1 or 2.")
        choose_mode()

def cli_mode():
    length = int(input("Enter password length (8-20): "))
    if length < 8 or length > 20:
        print("Password length must be between 8 and 20 characters.")
        return
    
    use_alpha = input("Include alphabets (y/n)? ").lower() == "y"
    use_digits = input("Include digits (0-9) (y/n)? ").lower() == "y"
    use_symbols = input("Include symbols (@#$%&*!) (y/n)? ").lower() == "y"
    exclude_chars = input("Enter characters to exclude (optional): ")
    
    try:
        password = generate_password_cli(length, use_alpha, use_digits, use_symbols, exclude_chars)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)

def generate_password_cli(length, use_alpha, use_digits, use_symbols, exclude_chars):
    characters = ""
    if use_alpha:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    characters = ''.join(c for c in characters if c not in exclude_chars)
    
    if not characters:
        raise ValueError("You must select at least one character type.")
    
    password = []
    if use_alpha:
        password.append(secrets.choice(string.ascii_letters))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))
    
    remaining_length = length - len(password)
    password += [secrets.choice(characters) for _ in range(remaining_length)]
    random.shuffle(password)
    
    return "".join(password)

def gui_mode():
    global root, length_var, alpha_var, digits_var, symbols_var, exclude_var, generated_password
    
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x350")
    root.resizable(False, False)

    tk.Label(root, text="Password Length (8-20):").pack()
    length_var = tk.StringVar(value="12")
    length_entry = ttk.Entry(root, textvariable=length_var, width=5)
    length_entry.pack()

    alpha_var = tk.BooleanVar(value=True)
    digits_var = tk.BooleanVar(value=True)
    symbols_var = tk.BooleanVar(value=False)

    ttk.Checkbutton(root, text="Include Alphabets", variable=alpha_var).pack()
    ttk.Checkbutton(root, text="Include Digits", variable=digits_var).pack()
    ttk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

    tk.Label(root, text="Exclude Characters:").pack()
    exclude_var = tk.StringVar()
    exclude_entry = ttk.Entry(root, textvariable=exclude_var, width=20)
    exclude_entry.pack()

    generated_password = tk.StringVar()

    generate_btn = ttk.Button(root, text="Generate Password", command=generate_password)
    generate_btn.pack(pady=5)

    ttk.Entry(root, textvariable=generated_password, state="readonly", width=30).pack()
    copy_btn = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
    copy_btn.pack(pady=5)

    root.mainloop()

choose_mode()
