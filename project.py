import tkinter as tk
from tkinter import ttk

# Define a function to collect user input for workout goals and preferences
def collect_user_input():
    name = name_entry.get()
    age = age_entry.get()
    weight = weight_entry.get()
    height = height_entry.get()
    goals = goals_entry.get()
    preferences = preferences_entry.get("1.0", tk.END).strip()  # Get text from Text widget

    # Display gathered information in console (replace with your logic)
    print("Name:", name)
    print("Age:", age)
    print("Weight:", weight)
    print("Height:", height)
    print("Fitness Goals:", goals)
    print("Dietary preferences or health conditions:", preferences)

# Create the main window
root = tk.Tk()
root.title("Personalized Workout App")

# Add labels and entry fields
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0, sticky="w")
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

tk.Label(root, text="Weight (kg):").grid(row=2, column=0, sticky="w")
weight_entry = tk.Entry(root)
weight_entry.grid(row=2, column=1)

tk.Label(root, text="Height (m):").grid(row=3, column=0, sticky="w")
height_entry = tk.Entry(root)
height_entry.grid(row=3, column=1)

tk.Label(root, text="Fitness Goals:").grid(row=4, column=0, sticky="w")
goals_entry = tk.Entry(root)
goals_entry.grid(row=4, column=1)

tk.Label(root, text="Dietary Preferences or Health Conditions:").grid(row=5, column=0, sticky="w")
preferences_entry = tk.Text(root, height=4, width=30)
preferences_entry.grid(row=5, column=1)

# Button to collect user input
submit_button = ttk.Button(root, text="Submit", command=collect_user_input)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()

# Call the function to start collecting user input
collect_user_input()