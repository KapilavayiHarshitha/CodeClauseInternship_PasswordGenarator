#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_numbers = numbers_var.get()
    use_special_chars = special_chars_var.get()

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        result_label.config(text="Select at least one character type")
        return

    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_result.set(password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_chars_var = tk.BooleanVar()

uppercase_check = tk.Checkbutton(root, text="Uppercase", variable=uppercase_var)
lowercase_check = tk.Checkbutton(root, text="Lowercase", variable=lowercase_var)
numbers_check = tk.Checkbutton(root, text="Numbers", variable=numbers_var)
special_chars_check = tk.Checkbutton(root, text="Special Characters", variable=special_chars_var)

uppercase_check.grid(row=1, column=0)
lowercase_check.grid(row=2, column=0)
numbers_check.grid(row=3, column=0)
special_chars_check.grid(row=4, column=0)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2)

password_result = tk.StringVar()
result_entry = tk.Entry(root, textvariable=password_result)
result_entry.grid(row=7, column=0, columnspan=2)

root.mainloop()


# In[ ]:




