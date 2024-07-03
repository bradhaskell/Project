import tkinter as tk
from tkinter import ttk

# Global variables to store user input
user_data = {}

# Define a function to collect user input for workout goals and preferences
def collect_user_input(event=None):
    global user_data
    user_data['name'] = name_entry.get()
    user_data['age'] = age_entry.get()
    user_data['weight'] = weight_entry.get()
    user_data['height'] = height_entry.get()
    user_data['goals'] = goals_combobox.get()
    user_data['preferences'] = preferences_entry.get("1.0", tk.END).strip()  # Get text from Text widget
    
    show_results()

# Define a function to display the collected user information in a new window
def show_results():
    results_window = tk.Toplevel(root)
    results_window.title("Your Workout Plan")

    # Create labels to display the collected information with better font
    font_label = ('Arial', 12)  # Define a font style (change as needed)
    
    tk.Label(results_window, text="Name:", font=font_label).grid(row=0, column=0, sticky="w")
    tk.Label(results_window, text=user_data['name'], font=font_label).grid(row=0, column=1)

    tk.Label(results_window, text="Age:", font=font_label).grid(row=1, column=0, sticky="w")
    tk.Label(results_window, text=user_data['age'], font=font_label).grid(row=1, column=1)

    tk.Label(results_window, text="Weight (kg):", font=font_label).grid(row=2, column=0, sticky="w")
    tk.Label(results_window, text=user_data['weight'], font=font_label).grid(row=2, column=1)

    tk.Label(results_window, text="Height (m):", font=font_label).grid(row=3, column=0, sticky="w")
    tk.Label(results_window, text=user_data['height'], font=font_label).grid(row=3, column=1)

    tk.Label(results_window, text="Fitness Goals:", font=font_label).grid(row=4, column=0, sticky="w")
    tk.Label(results_window, text=user_data['goals'], font=font_label).grid(row=4, column=1)

    tk.Label(results_window, text="Dietary Preferences or Health Conditions:", font=font_label).grid(row=5, column=0, sticky="w")
    tk.Label(results_window, text=user_data['preferences'], font=font_label).grid(row=5, column=1)

    # Button to close the results window
    ttk.Button(results_window, text="Close", command=results_window.destroy).grid(row=6, column=0, columnspan=2, pady=10)

# Create the main window
root = tk.Tk()
root.title("FitFlow")

# Set window size and position (change as needed)
window_width = 800
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)
root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

# Set font style for labels and entry fields (change as needed)
font_label_entry = ('Arial', 12)

# Add labels and entry fields with better font
tk.Label(root, text="Name:", font=font_label_entry).grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(root, font=font_label_entry)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Age:", font=font_label_entry).grid(row=1, column=0, sticky="w")
age_entry = tk.Entry(root, font=font_label_entry)
age_entry.grid(row=1, column=1)

tk.Label(root, text="Weight (kg):", font=font_label_entry).grid(row=2, column=0, sticky="w")
weight_entry = tk.Entry(root, font=font_label_entry)
weight_entry.grid(row=2, column=1)

tk.Label(root, text="Height (m):", font=font_label_entry).grid(row=3, column=0, sticky="w")
height_entry = tk.Entry(root, font=font_label_entry)
height_entry.grid(row=3, column=1)

tk.Label(root, text="Fitness Goals:", font=font_label_entry).grid(row=4, column=0, sticky="w")
# Dropdown list for fitness goals
fitness_goals = ['Lose weight', 'Build muscle', 'Increase endurance', 'Improve flexibility', 'Maintain overall health']
goals_combobox = ttk.Combobox(root, values=fitness_goals, font=font_label_entry)
goals_combobox.grid(row=4, column=1)

tk.Label(root, text="Dietary Preferences or Health Conditions:", font=font_label_entry).grid(row=5, column=0, sticky="w")
preferences_entry = tk.Text(root, height=4, width=30, font=font_label_entry)
preferences_entry.grid(row=5, column=1)

# Button to collect user input
submit_button = ttk.Button(root, text="Submit", command=collect_user_input, style='TButton')
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Bind Enter key to submit_button
root.bind('<Return>', collect_user_input)

# Start the main event loop
root.mainloop()