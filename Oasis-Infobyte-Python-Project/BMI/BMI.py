import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from datetime import datetime
import json
import os

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x500")
        
        # Data storage
        self.data_file = "bmi_history.json"
        self.history = self.load_history()
        
        # GUI Elements
        tk.Label(root, text="BMI Calculator", font=("Arial", 16)).pack(pady=10)
        
        # Name input
        tk.Label(root, text="Name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        
        # Weight input
        tk.Label(root, text="Weight (kg):").pack()
        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()
        
        # Height input
        tk.Label(root, text="Height (m):").pack()
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()
        
        # Buttons
        tk.Button(root, text="Calculate BMI", command=self.calculate_bmi).pack(pady=10)
        tk.Button(root, text="View History", command=self.show_history).pack(pady=5)
        
        # Result display
        self.result_label = tk.Label(root, text="", wraplength=350)
        self.result_label.pack(pady=10)

    def calculate_bmi(self):
        try:
            # Get and validate inputs
            name = self.name_entry.get().strip()
            if not name:
                raise ValueError("Please enter a name")
                
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            
            if weight <= 0 or weight > 500:
                raise ValueError("Weight must be between 0 and 500 kg")
            if height <= 0 or height > 3:
                raise ValueError("Height must be between 0 and 3 meters")
            
            # Calculate BMI
            bmi = weight / (height ** 2)
            
            # Determine category
            category = self.get_bmi_category(bmi)
            
            # Display result
            result = f"BMI: {bmi:.1f}\nCategory: {category}"
            self.result_label.config(text=result)
            
            # Save to history
            self.save_to_history(name, weight, height, bmi, category)
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input! Please enter numeric values")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def save_to_history(self, name, weight, height, bmi, category):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "weight": weight,
            "height": height,
            "bmi": bmi,
            "category": category
        }
        
        if name not in self.history:
            self.history[name] = []
        self.history[name].append(entry)
        
        with open(self.data_file, 'w') as f:
            json.dump(self.history, f, indent=2)

    def load_history(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {}

    def show_history(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter a name to view history")
            return
            
        if name in self.history and self.history[name]:
            # Create graph
            dates = [entry["timestamp"] for entry in self.history[name]]
            bmis = [entry["bmi"] for entry in self.history[name]]
            
            plt.figure(figsize=(10, 5))
            plt.plot(dates, bmis, 'b-o')
            plt.title(f"BMI Trend for {name}")
            plt.xlabel("Date")
            plt.ylabel("BMI")
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            
            # Show detailed history
            history_text = f"History for {name}:\n\n"
            for entry in self.history[name]:
                history_text += (f"Date: {entry['timestamp']}\n"
                               f"BMI: {entry['bmi']:.1f} - {entry['category']}\n"
                               f"Weight: {entry['weight']}kg, Height: {entry['height']}m\n\n")
            messagebox.showinfo("BMI History", history_text)
        else:
            messagebox.showinfo("History", f"No history found for {name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()