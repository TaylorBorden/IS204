"""
Payroll Calculator GUI Application

This script creates a graphical user interface (GUI) application for calculating and saving the gross pay of employees.
The application allows the user to input employee details, calculate their gross pay including overtime, save the data
to a file, clear the inputs, and close the file.

Classes:
    PayrollApp: The main application class that handles the GUI and its functionalities.

Functions:
    __init__(self, root): Initializes the main application window and widgets.
    create_widgets(self): Creates and places the widgets in the application window.
    calculate_gross_pay(self): Calculates the gross pay of the employee based on the input hours and wage.
    save_data(self): Saves the employee's data and calculated gross pay to a CSV file.
    clear_entries(self): Clears the input textboxes and result label.
    close_file(self): Closes the currently open file.

Usage:
    - Run the script to open the application window.
    - Enter employee details in the provided textboxes.
    - Click 'Calculate Gross Pay' to compute the gross pay.
    - Click 'Save Data' to save the employee's data and gross pay to a file.
    - Click 'Clear' to reset the inputs and results.
    - Click 'Close File' to close the open file.

Author:
    [Taylor Borden] - Created for [IS204] Date - [11/10/2024]
"""

import tkinter as tk
from tkinter import filedialog, messagebox

class PayrollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll Calculator")
        self.root.geometry("400x400")  # Set the window size to 400x400 pixels
        self.root.configure(bg='#36454F')  
        
        self.file = None

        # Labels and Textboxes
        self.create_widgets()

    def create_widgets(self):
        # Define color scheme
        label_fg_color = '#FFFFFF'  # White for label text
        entry_bg_color = '#2F4F4F'  # Dark Slate Gray for entry background
        entry_fg_color = '#FFFFFF'  # White for entry text
        button_bg_color = '#4682B4'  # Steel Blue for button background
        button_fg_color = '#FFFFFF'  # White for button text
        result_label_color = '#00FF00'  # Bright green for result label text

        tk.Label(self.root, text="First Name:", bg='#36454F', fg=label_fg_color).grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.first_name_entry = tk.Entry(self.root, bg=entry_bg_color, fg=entry_fg_color)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Last Name:", bg='#36454F', fg=label_fg_color).grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.last_name_entry = tk.Entry(self.root, bg=entry_bg_color, fg=entry_fg_color)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Hours Worked:", bg='#36454F', fg=label_fg_color).grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.hours_worked_entry = tk.Entry(self.root, bg=entry_bg_color, fg=entry_fg_color)
        self.hours_worked_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Hourly Wage:", bg='#36454F', fg=label_fg_color).grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.hourly_wage_entry = tk.Entry(self.root, bg=entry_bg_color, fg=entry_fg_color)
        self.hourly_wage_entry.grid(row=3, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(self.root, text="Calculate Gross Pay", command=self.calculate_gross_pay, bg=button_bg_color, fg=button_fg_color)
        self.calculate_button.grid(row=4, columnspan=2, pady=10)

        self.save_button = tk.Button(self.root, text="Save Data", command=self.save_data, bg=button_bg_color, fg=button_fg_color)
        self.save_button.grid(row=5, columnspan=2, pady=10)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_entries, bg=button_bg_color, fg=button_fg_color)
        self.clear_button.grid(row=6, columnspan=2, pady=10)

        self.close_button = tk.Button(self.root, text="Close File", command=self.close_file, bg='#800000', fg=button_fg_color)  
        self.close_button.grid(row=7, columnspan=2, pady=10)

        self.result_label = tk.Label(self.root, text="", fg=result_label_color, bg='#36454F', font=('Arial', 14, 'bold'))
        self.result_label.grid(row=8, columnspan=2, pady=10)

    def calculate_gross_pay(self):
        try:
            hours = float(self.hours_worked_entry.get())
            wage = float(self.hourly_wage_entry.get())
            if hours > 40:
                gross_pay = 40 * wage + (hours - 40) * wage * 1.5
            else:
                gross_pay = hours * wage
            self.result_label.config(text=f"Gross Pay: ${gross_pay:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for hours and wage.")

    def save_data(self):
        if not self.file:
            self.file = filedialog.asksaveasfile(mode='w', defaultextension=".csv", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))

        if self.file:
            try:
                first_name = self.first_name_entry.get()
                last_name = self.last_name_entry.get()
                hours_worked = self.hours_worked_entry.get()
                hourly_wage = self.hourly_wage_entry.get()
                gross_pay = self.result_label.cget("text").split("$")[1]

                self.file.write(f"{first_name},{last_name},{hours_worked},{hourly_wage},{gross_pay}\n")
                self.result_label.config(text=f"Data saved for {first_name} {last_name}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save data: {e}")

    def clear_entries(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.hours_worked_entry.delete(0, tk.END)
        self.hourly_wage_entry.delete(0, tk.END)
        self.result_label.config(text="")

    def close_file(self):
        if self.file:
            self.file.close()
            self.file = None
            self.result_label.config(text="File closed")

if __name__ == "__main__":
    root = tk.Tk()
    app = PayrollApp(root)
    root.mainloop()
