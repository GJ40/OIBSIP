import customtkinter as ctk
import pyperclip
import random
import string


# functions
def copy_to_clipboard():
    content = password_string.get()
    pyperclip.copy(content)


def shuffling(password):
    lst = list(password)
    random.shuffle(lst)
    password = ''.join(lst)
    return password


def generate_password():
    uppercase_letters = list(string.ascii_uppercase)
    lowercase_letters = list(string.ascii_lowercase)
    numbers = list(string.digits)
    symbols = list('!@#$%^&*?_')
    password = ""
    upperl = int(uppercase_letters_count.get())
    lowerl = int(lowercase_letters_count.get())
    n = int(numbers_count.get())
    s = int(symbols_count.get())
    password = password.join(random.choices(uppercase_letters, k=upperl) + random.choices(lowercase_letters, k=lowerl) +
                             random.choices(numbers, k=n) + random.choices(symbols, k=s))
    password = shuffling(password)
    password_string.set(password)


# main window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
window = ctk.CTk()
window.title('Password_Generator')
window.geometry('500x400')
window.columnconfigure(0, weight=1)
window.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
window.resizable(True, False)

# Top Label
Heading = ctk.CTkLabel(master=window, text='Random_Password', font=('Calibri bold', 40))
Heading.grid(row=0, column=0)

# Input Frame
input_frame = ctk.CTkFrame(master=window)
input_frame.grid(row=1, column=0,rowspan=2)
input_frame.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')

# labels
uppercase_letter_label = ctk.CTkLabel(master=input_frame, text='uppercase\nletters', font=('Calibri bold', 20))
uppercase_letter_label.grid(row=0, column=0, padx=5, pady=5)

lowercase_letter_label = ctk.CTkLabel(master=input_frame, text='lowercase\nletters', font=('Calibri bold', 20))
lowercase_letter_label.grid(row=0, column=1, padx=5, pady=5)

number_label = ctk.CTkLabel(master=input_frame, text='numbers', font=('Calibri bold', 20))
number_label.grid(row=0, column=2, padx=5, pady=5)

symbol_label = ctk.CTkLabel(master=input_frame, text='symbols', font=('Calibri bold', 20))
symbol_label.grid(row=0, column=3, padx=5, pady=5)

# Entries
uppercase_letters_count = ctk.StringVar()
uppercase_letters_count.set('0')
uppercase_letter_entry = ctk.CTkEntry(master=input_frame, textvariable=uppercase_letters_count, justify='center',
                                font=('Calibri bold', 20))
uppercase_letter_entry.grid(row=1, column=0, padx=5, pady=5)

lowercase_letters_count = ctk.StringVar()
lowercase_letters_count.set('0')
lowercase_letter_entry = ctk.CTkEntry(master=input_frame, textvariable=lowercase_letters_count, justify='center',
                                font=('Calibri bold', 20))
lowercase_letter_entry.grid(row=1, column=1, padx=5, pady=5)




numbers_count = ctk.StringVar()
numbers_count.set('0')
number_entry = ctk.CTkEntry(master=input_frame, textvariable=numbers_count, justify='center',
                            font=('Calibri bold', 20))
number_entry.grid(row=1, column=2, padx=5, pady=5)

symbols_count = ctk.StringVar()
symbols_count.set('0')
symbol_entry = ctk.CTkEntry(master=input_frame, textvariable=symbols_count, justify='center',
                                font=('Calibri bold', 20))
symbol_entry.grid(row=1, column=3, padx=5, pady=5)


# output field
output_frame = ctk.CTkFrame(master=window)
output_frame.grid(row=4, column=0)

password_string = ctk.StringVar()
password_label = ctk.CTkLabel(master=output_frame, text='.....', textvariable=password_string,
                              font=('Calibri bold', 20))
password_label.pack(side='left', padx=10, pady=10)

# Copy button
copy_button = ctk.CTkButton(master=output_frame, text='copy', font=('Calibri bold', 20), command=copy_to_clipboard)
copy_button.pack(side='left', padx=10, pady=10)

# Generate Password Button
generate_button = ctk.CTkButton(master=window, text='Generate_Password', font=('Calibri bold', 30),
                                command=generate_password)
generate_button.grid(row=3, column=0, padx=50, pady=10)

window.mainloop()
