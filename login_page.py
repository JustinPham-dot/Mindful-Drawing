import tkinter as tk
from tkinter import messagebox
from draw_page import DrawingApp  # Importing the DrawingApp class from draw_page.py 

# Dummy database of registered users
registered_users = {"admin": "password"}

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if username and password match any registered user
    if username in registered_users and registered_users[username] == password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        # Open the DrawingApp when login is successful
        root.withdraw()  # Hide the login window
        draw_window = tk.Toplevel(root)
        draw_window.title("Drawing App")
        app = DrawingApp(draw_window, draw_window)  # Create an instance of DrawingApp
        app.draw_menu()  # Draw the menu in DrawingApp
        # Bind the function to the closing event of the drawing window
        draw_window.protocol("WM_DELETE_WINDOW", lambda: close_drawing_window(draw_window))
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def clear_fields():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

def register():
    new_username = entry_new_username.get()
    new_password = entry_new_password.get()

    # Add new user to the registered users database
    registered_users[new_username] = new_password
    messagebox.showinfo("Registration Successful", "Registration successful for user: " + new_username)
    # Destroy the registration window after registration is successful
    register_window.destroy()

def open_register_page():
    global register_window
    register_window = tk.Toplevel(root)
    register_window.title("Register Page")

    label_register = tk.Label(register_window, text="Registration Form")
    label_register.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

    # New Username Label and Entry
    label_new_username = tk.Label(register_window, text="<b>New Username:</b>")
    label_new_username.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

    global entry_new_username
    entry_new_username = tk.Entry(register_window)
    entry_new_username.grid(row=1, column=1, padx=10, pady=5)

    # New Password Label and Entry
    label_new_password = tk.Label(register_window, text="New Password:")
    label_new_password.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)

    global entry_new_password
    entry_new_password = tk.Entry(register_window, show="*")
    entry_new_password.grid(row=2, column=1, padx=10, pady=5)

    # Register Button
    button_register = tk.Button(register_window, text="Register", command=register, bg="yellow", fg="white")
    button_register.grid(row=3, column=0, columnspan=2, pady=10)

def close_drawing_window(window):
    messagebox.showinfo("Closing", "Thanks for drawing!")
    window.destroy()

# Create main window
root = tk.Tk()
root.title("LOGIN!")

# Title Label
label_title_2 = tk.Label(root, text="Welcome to DrawingApp", font=("Arial", 14, "bold"),fg="Purple")
label_title_2.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

# Username Label and Entry
label_username = tk.Label(root, text="Username:", font=("Arial", 10, "bold"))
label_username.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

entry_username = tk.Entry(root)
entry_username.grid(row=1, column=1, padx=10, pady=5)

# Password Label and Entry
label_password = tk.Label(root, text="Password:", font=("Arial", 10, "bold"))
label_password.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=5)

# Clear Button
button_clear = tk.Button(root, text="Clear", font=("Arial", 9, "bold"), command=clear_fields)
button_clear.grid(row=3, column=0, columnspan=1, pady=15)
button_clear.config(bg="green", fg="white")

# Login Button
button_login = tk.Button(root, text="Login", font=("Arial", 9, "bold"), command=login)
button_login.grid(row=3, column=1, columnspan=1, pady=15)
button_login.config(bg="green", fg="white")

# Register Link
label_register_link = tk.Label(root, text="Don't have an account? Register here", fg="blue", cursor="hand2")
label_register_link.grid(row=4, column=0, columnspan=2, pady=5)
label_register_link.bind("<Button-1>", lambda event: open_register_page())

# Run the main event loop
root.mainloop()
