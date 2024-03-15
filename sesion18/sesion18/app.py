import tkinter as tk
from tkinter import ttk

root = tk.Tk()
#crear frame
main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

main2 = ttk.Frame(master=main)
main2.pack(side="left", fill="both")

tk.Label(main, text="Etiqueta 1", bg="green").pack(side="top", expand=True, fill="both")
tk.Label(main, text="Etiqueta 2", bg="green").pack(side=tk.TOP, expand=True, fill="both")
tk.Label(master=main2, text="Etiqueta 3", bg="blue").pack(side=tk.LEFT, expand=True, fill="both")

root.mainloop()

