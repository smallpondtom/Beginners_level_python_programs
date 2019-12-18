#%%
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=500, height=500)
canvas1.pack()

button1 = tk.Button(root, text='Exit this Canvas', command=root.destroy)
canvas1.create_window(250, 250, window=button1)


# closing the canvas automatically after 30 seconds 
root.after(5000, lambda: root.destroy())
root.mainloop()
#%%