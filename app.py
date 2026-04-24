import tkinter as tk

def show_text():
    print(entry.get())

root = tk.Tk()
root.title("My App")
root.geometry("400x300")

entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Submit", command=show_text)
button.pack()

root.mainloop()

