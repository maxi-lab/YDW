import tkinter as tk
import pytube

if __name__ == "__main__":
    root=tk.Tk()
    root.title("Yout DW")
    root.minsize(300,300)
    tk.Label(root,text="Ingresa el link aquí").pack()
    entrada=tk.Entry()
    entrada.pack()
    tk.Button(text="Descarga").pack()
    root.mainloop()