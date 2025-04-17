# gui.py (English Version)
import tkinter as tk
from tkinter import ttk, messagebox
from logic import calculate_salary, grade_data, marital_bonus, experience_bonus

def update_result(result):
    if not result:
        return
    entries = [
        base_entry, family_entry, children_bonus_entry,
        experience_entry, ir_entry, cnss_entry, net_salary_entry
    ]
    values = [
        result["base"], result["family"], result["children_bonus"],
        result["experience"], result["ir"], result["cnss"], result["net"]
    ]
    for entry, val in zip(entries, values):
        entry.config(state=tk.NORMAL)
        entry.delete(0, tk.END)
        entry.insert(0, str(val))
        entry.config(state=tk.DISABLED)

def clear_fields():
    for widget in [grade_combo, marital_combo, experience_combo]:
        widget.set("")
    children_entry.delete(0, tk.END)
    for entry in [base_entry, family_entry, children_bonus_entry, experience_entry, ir_entry, cnss_entry, net_salary_entry]:
        entry.config(state=tk.NORMAL)
        entry.delete(0, tk.END)
        entry.config(state=tk.DISABLED)

def calculate_and_display():
    result = calculate_salary(
        grade_combo.get(),
        marital_combo.get(),
        experience_combo.get(),
        children_entry.get()
    )
    update_result(result)

def create_main_window():
    window = tk.Tk()
    window.title("Salary Calculator")
    window.geometry("800x500")

    def label(text, x, y):
        tk.Label(window, text=text).place(x=x, y=y)

    label("Grade:", 60, 50)
    label("Marital Status:", 60, 90)
    label("Number of Children:", 60, 130)
    label("Experience:", 60, 170)
    label("Base Salary:", 60, 210)
    label("Family Bonus:", 60, 250)
    label("Children Bonus:", 60, 290)
    label("Experience Bonus:", 60, 330)
    label("IR:", 60, 370)
    label("CNSS:", 60, 410)
    label("Net Salary:", 60, 450)

    global grade_combo, marital_combo, experience_combo, children_entry
    global base_entry, family_entry, children_bonus_entry, experience_entry, ir_entry, cnss_entry, net_salary_entry

    grade_combo = ttk.Combobox(window, values=list(grade_data.keys()))
    grade_combo.place(x=250, y=50)

    marital_combo = ttk.Combobox(window, values=list(marital_bonus.keys()))
    marital_combo.place(x=250, y=90)

    children_entry = tk.Entry(window)
    children_entry.place(x=250, y=130)

    experience_combo = ttk.Combobox(window, values=list(experience_bonus.keys()))
    experience_combo.place(x=250, y=170)

    def make_entry(x, y):
        entry = tk.Entry(window, state=tk.DISABLED)
        entry.place(x=x, y=y)
        return entry

    base_entry = make_entry(250, 210)
    family_entry = make_entry(250, 250)
    children_bonus_entry = make_entry(250, 290)
    experience_entry = make_entry(250, 330)
    ir_entry = make_entry(250, 370)
    cnss_entry = make_entry(250, 410)
    net_salary_entry = make_entry(250, 450)

    tk.Button(window, text="Calculate", command=calculate_and_display).place(x=500, y=100)
    tk.Button(window, text="Clear", command=clear_fields).place(x=500, y=140)
    tk.Button(window, text="Exit", command=window.destroy).place(x=500, y=180)

    window.mainloop()

def start_app():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x200")

    tk.Label(login_window, text="Username:").place(x=50, y=50)
    tk.Label(login_window, text="Password:").place(x=50, y=90)

    username_entry = tk.Entry(login_window)
    username_entry.place(x=150, y=50)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.place(x=150, y=90)

    def attempt_login():
        if username_entry.get() == "ayoub" and password_entry.get() == "ayb":
            login_window.destroy()
            create_main_window()
        else:
            messagebox.showerror("Error", "Incorrect username or password")

    tk.Button(login_window, text="Login", command=attempt_login).place(x=150, y=140)
    login_window.mainloop()

if __name__ == '__main__':
    start_app()
