import tkinter

window = tkinter.Tk()
window.title("MY GUI")
window.minsize(height= 500, width = 500)

# Lable
my_label = tkinter.Label(text = "i am a Lable", font = ("Arial", 24, "bold"))
my_label.pack(side = "top")

window.mainloop()
