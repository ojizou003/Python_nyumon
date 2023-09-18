import tkinter

window1=tkinter.Tk()

def tojiru():
  window1.quit()
def resize():
  window1.geometry("300x300")

button1 = tkinter.Button(master=window1,text="Push me",command=tojiru)
button1.pack()
button2 = tkinter.Button(master=window1,text="Resize",command=resize)
button2.pack()

window1.mainloop()