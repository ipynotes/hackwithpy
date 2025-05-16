import tkinter as tk
from tkinter import simpledialog
import test


# Function to execute when the button is clicked



# Creating main window
root = tk.Tk()
root.title("MasterPassword")
#root.geometry("500x250")
root.iconbitmap("snake.ico")
root.configure(bg="#3A3A3A")
root.tk_setPalette(background="#3A3A3A", foreground="white")
root.resizable(False, False)

# Define window size
window_width = 500
window_height = 250

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position for center alignment
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the window position
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


# Add a header space
header = tk.Label(root, text=" ", height=1,bg="#3A3A3A")  # Creates space
header.grid(row=0, columnspan=2)

mpassword = simpledialog.askstring("Login", "Enter MasterPassword:", show="*")

# Labels and Entry fields
labels = ["Site", "Counter", "Context", "Length", "PASSWORD"]
entries = {}

for i, label in enumerate(labels):
    i2 = i + 1
    tk.Label(root, text=label,fg="white", bg="#3A3A3A").grid(row=i2, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(root,width=50,bg="#4E4E4E", fg="white")
    entry.grid(row=i2, column=1, padx=10, pady=5)
    entries[label.lower()] = entry  # Store entries in a dictionary



# Assign entries to individual variables
site_entry = entries["site"]
counter_entry = entries["counter"]
context_entry = entries["context"]
length_entry = entries["length"]
gen_password = entries["password"]
name = "com.masterpassword.v3"




def OnClick():
    print("Execute button clicked!")
    print("Site:", site_entry.get())
    print("Counter:", counter_entry.get())
    print("Context:", context_entry.get())
    print("Length:", length_entry.get())
    #print("Password:", password_entry.get())
    ununique_password,safe_password = test.generate_unique_string(name, mpassword, site_entry.get(), counter_entry.get(), context_entry.get(), length_entry.get())
    gen_password.delete(0, tk.END) 
    gen_password.insert(0,safe_password) #unique_string



# Execute button
execute_button = tk.Button(root, text="Execute", command=OnClick)
execute_button.grid(row=len(labels)+1, columnspan=2, pady=10)

# Run the application
root.mainloop()
