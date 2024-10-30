import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
class DataVisualizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pie Chart Visualization Tool")
        self.data_frame = tk.Frame(root)
        self.data_frame.pack(pady=20)
        self.category_label = tk.Label(self.data_frame, text="Category:")
        self.category_label.grid(row=0, column=0)
        self.category_entry = tk.Entry(self.data_frame)
        self.category_entry.grid(row=0, column=1)
        self.value_label = tk.Label(self.data_frame, text="Value:")
        self.value_label.grid(row=1, column=0)
        self.value_entry = tk.Entry(self.data_frame)
        self.value_entry.grid(row=1, column=1)
        self.add_button = tk.Button(root, text="Add Data Point", command=self.add_data)
        self.add_button.pack(pady=10)
        self.plot_button = tk.Button(root, text="Plot Pie Chart", command=self.plot_data, state=tk.DISABLED)
        self.plot_button.pack(pady=10)
        self.data = {}
    def add_data(self):
        category = self.category_entry.get()
        try:
            value = float(self.value_entry.get())
            if category in self.data:
                self.data[category] += value  
            else:
                self.data[category] = value           
            messagebox.showinfo("Success", "Data point added successfully!")
            self.category_entry.delete(0, tk.END)
            self.value_entry.delete(0, tk.END)
            self.plot_button.config(state=tk.NORMAL)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric value for the value field.")
    def plot_data(self):
        if self.data:
            categories = list(self.data.keys())
            values = list(self.data.values())
            plt.figure(figsize=(8, 8))
            plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
            plt.title("Pie Chart Visualization")
            plt.axis('equal') 
            plt.show()
        else:
            messagebox.showerror("Error", "No data to plot. Please add data points.")
if __name__ == "__main__":
    root = tk.Tk()
    app = DataVisualizationApp(root)
    root.mainloop()
    