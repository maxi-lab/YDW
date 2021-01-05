import tkinter as tk


if __name__ == "__main__":
    root=tk.Tk()
    root.title("Yout DW")
    root.minsize(300,300)
    tk.Label(root,text="Ingresa el link aquí").pack()
    root.mainloop()