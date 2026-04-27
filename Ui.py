import tkinter as tk

root = tk.Tk()

root.geometry("400x500")
root.title("Banking App")

label = tk.Label(root, text="Welcome to the Banking App!", font=("Roman", 16))
label.pack(padx=20, pady=20)


text = tk.Text(root, height=10, font=("Roman", 12))
text.pack(padx=20, pady=20)

def show_message():
    print("hello world")

btn1 = tk.Button(root, text="Submit", font=("Roman", 12), command=show_message)
btn1.pack(padx=20, pady=20)

    

root.mainloop()