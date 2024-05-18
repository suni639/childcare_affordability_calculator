import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import asksaveasfile, askopenfile
import matplotlib.pyplot as plt
from src.calculations import calculate_net_gain_loss
from src.utils import is_valid_number, format_currency, load_json_file, save_json_file

def calculate_financials(entry_fields):
    try:
        if not all(is_valid_number(entry_fields[field].get()) for field in entry_fields):
            raise ValueError("All fields must be valid numbers.")
        
        childcare_costs = float(entry_fields['childcare_costs'].get())
        parent1_net_income = float(entry_fields['parent1_net_income'].get())
        parent2_net_income = float(entry_fields['parent2_net_income'].get())
        expenses = float(entry_fields['expenses'].get())

        net_gain_loss = calculate_net_gain_loss(
            parent1_net_income, parent2_net_income, childcare_costs, expenses
        )

        result_message = (f"Total Household Income: {format_currency(parent1_net_income + parent2_net_income)}\n"
                          f"Total Childcare Costs: {format_currency(childcare_costs)}\n"
                          f"Total Expenses: {format_currency(expenses)}\n"
                          f"Net Gain/Loss: {format_currency(net_gain_loss)}")

        messagebox.showinfo("Calculation Result", result_message)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def reset_fields(entry_fields):
    for field in entry_fields.values():
        field.delete(0, tk.END)

def save_scenario(entry_fields):
    scenario = {key: entry.get() for key, entry in entry_fields.items()}
    file = asksaveasfile(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file:
        save_json_file(scenario, file.name)

def load_scenario(entry_fields):
    file = askopenfile(mode='r', filetypes=[("JSON files", "*.json")])
    if file:
        scenario = load_json_file(file.name)
        for key, value in scenario.items():
            entry_fields[key].delete(0, tk.END)
            entry_fields[key].insert(0, value)

def show_graph(entry_fields):
    try:
        if not all(is_valid_number(entry_fields[field].get()) for field in entry_fields):
            raise ValueError("All fields must be valid numbers.")
        
        childcare_costs = float(entry_fields['childcare_costs'].get())
        parent1_net_income = float(entry_fields['parent1_net_income'].get())
        parent2_net_income = float(entry_fields['parent2_net_income'].get())
        expenses = float(entry_fields['expenses'].get())

        total_income = parent1_net_income + parent2_net_income
        net_gain_loss = total_income - childcare_costs - expenses

        labels = ['Net Income', 'Childcare Costs', 'Expenses']
        sizes = [total_income, childcare_costs, expenses]
        colors = ['lightgreen', 'lightcoral', 'lightskyblue']

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(f"Net Gain/Loss: {format_currency(net_gain_loss)}")
        plt.show()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

def show_help():
    help_text = (
        "This application helps you calculate the affordability of childcare.\n\n"
        "Inputs:\n"
        "- Childcare Costs (£/month): Enter the monthly cost of childcare.\n"
        "- Parent 1 Net Income (£/month): Enter the monthly net income of the first parent.\n"
        "- Parent 2 Net Income (£/month): Enter the monthly net income of the second parent.\n"
        "- Expenses (£/month): Enter the monthly expenses.\n\n"
        "Features:\n"
        "- Calculate: Calculate the net gain/loss after childcare costs and expenses.\n"
        "- Reset: Clear all input fields.\n"
        "- Save Scenario: Save the current scenario to a file.\n"
        "- Load Scenario: Load a scenario from a file.\n"
        "- Show Graph: Display a pie chart of the income and expenses breakdown.\n"
    )
    messagebox.showinfo("Help and Guidance", help_text)

def start_app():
    app = tk.Tk()
    app.title("Childcare Affordability Calculator")
    app.geometry("400x500")

    style = ttk.Style(app)
    style.theme_use('clam')

    frame = ttk.Frame(app, padding="10 10 10 10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    entry_fields = {}
    labels = [
        "Childcare Costs (£/month):",
        "Parent 1 Net Income (£/month):",
        "Parent 2 Net Income (£/month):",
        "Expenses (£/month):"
    ]
    field_keys = ['childcare_costs', 'parent1_net_income', 'parent2_net_income', 'expenses']

    for i, label in enumerate(labels):
        ttk.Label(frame, text=label).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entry_fields[field_keys[i]] = ttk.Entry(frame)
        entry_fields[field_keys[i]].grid(row=i, column=1, padx=10, pady=5)

    btn_calculate = ttk.Button(frame, text="Calculate", command=lambda: calculate_financials(entry_fields))
    btn_calculate.grid(row=len(labels), column=0, padx=10, pady=10, sticky=tk.W)

    btn_reset = ttk.Button(frame, text="Reset", command=lambda: reset_fields(entry_fields))
    btn_reset.grid(row=len(labels), column=1, padx=10, pady=10, sticky=tk.E)

    btn_save = ttk.Button(frame, text="Save Scenario", command=lambda: save_scenario(entry_fields))
    btn_save.grid(row=len(labels)+1, column=0, padx=10, pady=10, sticky=tk.W)

    btn_load = ttk.Button(frame, text="Load Scenario", command=lambda: load_scenario(entry_fields))
    btn_load.grid(row=len(labels)+1, column=1, padx=10, pady=10, sticky=tk.E)

    btn_graph = ttk.Button(frame, text="Show Graph", command=lambda: show_graph(entry_fields))
    btn_graph.grid(row=len(labels)+2, column=0, padx=10, pady=10, sticky=tk.W)

    menu = tk.Menu(app)
    app.config(menu=menu)

    help_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="Help and Guidance", command=show_help)

    for child in frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    app.mainloop()
