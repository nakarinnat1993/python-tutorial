import tkinter as tk

def set_label():
    text_value = text_input.get()
    label.configure(text=text_value)

window = tk.Tk()
window.title("Window UI")
window.minsize(600, 600)

label = tk.Label(master=window, text='Hello world')
label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window, text='Update label', command=set_label)
ok_button.pack()


window.mainloop()