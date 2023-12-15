import tkinter as tk
from tkinter import ttk

def bmi_cal():
    try:
        weight = float(weight_val.get())
        height = float(height_val.get())
        bmi = round(weight / (height ** 2), 2)
        result_lal.config(text=f'Your BMI value: {bmi}')     
    except ValueError:
        result_lal.config(text='Use valid numbers for weight and height.')

window = tk.Tk()
window.title('Python BMI Calculator')

style = ttk.Style()
style.theme_use('default')

frame = ttk.Frame(window, padding='15')
frame.grid(row=0, column=0, padx=15, pady=15)

ttk.Label(frame, text='Weight(kg):').grid(row=0, column=0, padx=12, pady=12)
weight_val = ttk.Entry(frame)
weight_val.grid(row=0, column=1, padx=12, pady=12)

ttk.Label(frame, text='Height(M):').grid(row=1, column=0, padx=12, pady=12)
height_val = ttk.Entry(frame)
height_val.grid(row=1, column=1, padx=12, pady=12)

calculate_btn = ttk.Button(frame, text='BMI Calculate', command=bmi_cal)
calculate_btn.grid(row=2, column=0, columnspan=2, pady=12)

result_lal = ttk.Label(frame, text='')
result_lal.grid(row=3, column=0, columnspan=2, pady=12)

window.mainloop()
