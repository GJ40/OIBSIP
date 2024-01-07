import tkinter as tk
import ttkbootstrap as ttk


# Button functions
def bmi_calculator():
    if unit_button.config('text')[-1] == 'Imperial':
        w = weight.get()
        h = height.get() * 12
        result = w * 703 / h ** 2
        classify_bmi(result)
        result = str(result)
        bmi.set(result[0:5])
    else:
        w = weight.get()
        h = height.get()
        result = w / h ** 2
        classify_bmi(result)
        result = str(result)
        bmi.set(result[0:5])


def classify_bmi(bmi):
    if bmi < 18.5:
        result = "Underweight"
    elif 18.5 <= bmi < 25:
        result = "Normal weight"
    elif 25 <= bmi < 30:
        result = "Overweight"
    else:
        result = "Obese"
    remark.set(result)


def unitswitch():
    if unit_button.config('text')[-1] == 'Metric':
        unit_button.config(text='Imperial')
        wunit.set('lbs')
        hunit.set('feet')
    else:
        unit_button.config(text='Metric')
        wunit.set('kg')
        hunit.set('m')


window = ttk.Window(themename='darkly')
window.title('BMI_App')
window.geometry('400x500')
window.resizable(True, False)

window.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')
window.columnconfigure(0, weight=1)

bmi = tk.StringVar()
bmi.set('0.0')
remark = tk.StringVar()
ResultText = tk.Label(master=window, text='0.0', font='Calibri 80 bold', textvariable=bmi)
ResultText.grid(column=0, row=1, rowspan=2)
Remark = tk.Label(master=window, text='Average', textvariable=remark, font='Calibri 20 bold')
Remark.grid(column=0, row=3)

wunit = tk.StringVar()
wunit.set('kg')
weight_frame = tk.Frame(master=window)
weight_frame.grid(column=0, row=4, padx=5, pady=5)
weight_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
weight_label = tk.Label(master=weight_frame, text='Weight', font='Calibri 15 bold')
# weight_label.pack(side='left',padx=5,pady=5)
weight_label.grid(row=0, column=0, padx=5, pady=5)
weight = tk.DoubleVar()
entry_weight = tk.Entry(master=weight_frame, textvariable=weight)
# entry_weight.pack(side='left',padx=5,pady=5)
entry_weight.grid(row=0, column=1, padx=5, pady=5)
weight_unit_label = tk.Label(master=weight_frame, textvariable=wunit, font='Calibri 15 bold')
weight_unit_label.grid(row=0, column=2, padx=5, pady=5)

hunit = tk.StringVar()
hunit.set('m')
height_frame = tk.Frame(master=window)
height_frame.grid(column=0, row=5, padx=5, pady=5)
height_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
height_label = tk.Label(master=height_frame, text='Height', font='Calibri 15 bold')
height_label.grid(row=0, column=0, padx=5, pady=5)
height = tk.DoubleVar()
entry_height = tk.Entry(master=height_frame, textvariable=height)
entry_height.grid(row=0, column=1, padx=5, pady=5)
height_unit_label = tk.Label(master=height_frame, textvariable=hunit, font='Calibri 15 bold')
height_unit_label.grid(row=0, column=2, padx=5, pady=5)

# Buttons
topframe = tk.Frame(master=window)
topframe.grid(column=0, row=0)
unit_button = tk.Button(master=topframe, text='Metric', font='Calibri 10 bold', command=unitswitch)
unit_button.pack(side='left', padx=5, pady=5)
calculate_button = tk.Button(master=topframe, text='Calculate', font='Calibri 10 bold', command=bmi_calculator)
calculate_button.pack(side='left', padx=5, pady=5)

window.mainloop()
