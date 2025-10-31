import tkinter as tk
from tkinter import ttk, messagebox


def convert_temperature():
    try:
        temp = float(temp_entry.get())
        from_unit = from_box.get()
        to_unit = to_box.get()


        if from_unit == to_unit:
            result = temp

        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (temp * 9/5) + 32
            elif to_unit == "Kelvin":
                result = temp + 273.15

        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (temp - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (temp - 32) * 5/9 + 273.15

        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = temp - 273.15
            elif to_unit == "Fahrenheit":
                result = (temp - 273.15) * 9/5 + 32


        result_label.config(text=f"{result:.2f} °{to_unit[0]}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")


def reset_fields():
    temp_entry.delete(0, tk.END)
    result_label.config(text="Result will appear here")



root = tk.Tk()
root.title("🌡️ Temperature Converter")
root.geometry("420x350")
root.config(bg="#F7F9FB")

title_label = tk.Label(
    root,
    text="🌡️ Temperature Converter",
    font=("Poppins", 18, "bold"),
    bg="#F7F9FB",
    fg="#2C3E50"
)
title_label.pack(pady=15)


input_frame = tk.Frame(root, bg="#F7F9FB")
input_frame.pack(pady=10)


tk.Label(
    input_frame,
    text="Enter Temperature:",
    font=("Poppins", 12),
    bg="#F7F9FB"
).grid(row=0, column=0, padx=10, pady=5)

temp_entry = ttk.Entry(input_frame, width=18, font=("Poppins", 12))
temp_entry.grid(row=0, column=1, padx=10, pady=5)


units = ["Celsius", "Fahrenheit", "Kelvin"]

tk.Label(
    input_frame,
    text="From:",
    font=("Poppins", 12),
    bg="#F7F9FB"
).grid(row=1, column=0, padx=10, pady=5)

from_box = ttk.Combobox(input_frame, values=units, state="readonly", font=("Poppins", 11))
from_box.current(0)
from_box.grid(row=1, column=1, padx=10, pady=5)

tk.Label(
    input_frame,
    text="To:",
    font=("Poppins", 12),
    bg="#F7F9FB"
).grid(row=2, column=0, padx=10, pady=5)

to_box = ttk.Combobox(input_frame, values=units, state="readonly", font=("Poppins", 11))
to_box.current(1)
to_box.grid(row=2, column=1, padx=10, pady=5)

btn_frame = tk.Frame(root, bg="#F7F9FB")
btn_frame.pack(pady=10)

style = ttk.Style()
style.configure("TButton", font=("Poppins", 11), padding=6)

convert_btn = ttk.Button(btn_frame, text="Convert", command=convert_temperature)
convert_btn.grid(row=0, column=0, padx=10)

reset_btn = ttk.Button(btn_frame, text="Reset", command=reset_fields)
reset_btn.grid(row=0, column=1, padx=10)


result_label = tk.Label(
    root,
    text="Result will appear here",
    font=("Poppins", 14, "bold"),
    bg="#F7F9FB",
    fg="#1F618D"
)
result_label.pack(pady=20)


root.mainloop()
