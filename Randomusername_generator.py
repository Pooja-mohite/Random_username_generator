import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# Function to get a random adjective
def get_random_adjective():
    adjectives = ["Cool", "Happy", "Brave", "Smart", "Loyal", "Swift", "Shiny", "Fierce", "Kind", "Jolly"]
    return random.choice(adjectives)

# Function to get a random noun
def get_random_noun():
    nouns = ["Tiger", "Dragon", "Eagle", "Lion", "Panda", "Wolf", "Bear", "Hawk", "Fox", "Otter"]
    return random.choice(nouns)

# Function to generate a username
def generate_username():
    include_numbers = number_var.get()
    include_special_chars = special_char_var.get()
    username_length = length_var.get()

    adjective = get_random_adjective()
    noun = get_random_noun()
    username = adjective + noun

    if include_numbers:
        username += str(random.randint(10, 99))

    if include_special_chars:
        username += random.choice(string.punctuation)

    if username_length:
        try:
            username_length = int(username_length)
            if len(username) < username_length:
                extra_length = username_length - len(username)
                username += ''.join(random.choices(string.ascii_letters + string.digits, k=extra_length))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the length.")
            return

    result_label.config(
        text=f"Generated Username: {username}",
        fg="#ffffff",
        bg="#4caf50",  # Green background for the result
        font=("Roboto", 14, "bold"),
    )
    generated_usernames.append(username)

# Function to save usernames to a file
def save_usernames():
    if not generated_usernames:
        messagebox.showinfo("Info", "No usernames to save!")
        return

    try:
        with open("usernames.txt", "w") as file:
            file.write("\n".join(generated_usernames))
        messagebox.showinfo("Success", "Usernames saved to usernames.txt")
    except IOError:
        messagebox.showerror("Error", "Failed to save usernames.")

# Initialize the GUI application
app = tk.Tk()
app.title("Random Username Generator")
app.geometry("600x450")
app.configure(bg="#f3f4f6")  # Light gray background for modern look

# Variables for user preferences
number_var = tk.BooleanVar()
special_char_var = tk.BooleanVar()
length_var = tk.StringVar()
generated_usernames = []

# Title Frame
title_frame = tk.Frame(app, bg="#1E88E5", pady=15)
title_frame.pack(fill="x")
title_label = tk.Label(
    title_frame,
    text="Random Username Generator",
    font=("Roboto", 20, "bold"),
    fg="#ffffff",
    bg="#1E88E5",
)
title_label.pack()

# Main Frame
main_frame = tk.Frame(app, bg="#ffffff", padx=30, pady=30, relief="groove", bd=2)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Checkbox for including numbers
number_checkbox = ttk.Checkbutton(main_frame, text="Include Numbers", variable=number_var)
number_checkbox.grid(row=0, column=0, sticky="w", pady=10)

# Checkbox for including special characters
special_char_checkbox = ttk.Checkbutton(main_frame, text="Include Special Characters", variable=special_char_var)
special_char_checkbox.grid(row=1, column=0, sticky="w", pady=10)

# Entry for custom username length
length_label = tk.Label(main_frame, text="Desired Username Length (optional):", bg="#ffffff", font=("Roboto", 12))
length_label.grid(row=2, column=0, sticky="w", pady=10)
length_entry = ttk.Entry(main_frame, textvariable=length_var, width=25)
length_entry.grid(row=2, column=1, pady=10)

# Button to generate username
generate_button = ttk.Button(
    main_frame,
    text="Generate Username",
    command=generate_username,
    style="TButton",
)
generate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Label to display the generated username
result_label = tk.Label(
    main_frame,
    text="Generated Username: ",
    font=("Roboto", 12),
    bg="#ffffff",
    anchor="w",
)
result_label.grid(row=4, column=0, columnspan=2, pady=20, sticky="w")

# Button to save usernames to a file
save_button = ttk.Button(
    main_frame,
    text="Save Usernames",
    command=save_usernames,
    style="TButton",
)
save_button.grid(row=5, column=0, columnspan=2, pady=20)

# Footer
footer_label = tk.Label(
    app,
    text="Developed by PoojaM",
    font=("Roboto", 10),
    bg="#f3f4f6",
    fg="#888888",
)
footer_label.pack(side="bottom", pady=10)

# Modern Button Styling
style = ttk.Style()
style.configure(
    "TButton",
    font=("Roboto", 12),
    padding=10,
    background="#1E88E5",
    foreground="#ffffff",
    borderwidth=0,
    focuscolor="none",
)
style.map(
    "TButton",
    background=[("active", "#1565C0")],  # Darker blue on hover
)

# Run the GUI loop
app.mainloop()
