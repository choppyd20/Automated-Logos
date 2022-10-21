from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont


root = Tk()
helv36 = tkFont.Font(family='Helvetica', size=25, weight=tkFont.BOLD)
root.geometry("1920x1080")
root.attributes("-fullscreen",True)
root.configure(bg="DARK GRAY")
frm = ttk.Frame(root, padding=10)
frm.grid()
#ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

def gameMode():
    print("Beginning Game Code...")
def sensorMode():
    print("Testing Sensors...")
def motorMode():
    print("Testing Motors...")
    root.destroy()
    root2 = Tk()
    #helv36 = tkFont.Font(family='Helvetica', size=25, weight=tkFont.BOLD)
    root2.geometry("1920x1080")
    root2.attributes("-fullscreen",True)
    root2.configure(bg="DARK GRAY")
    frm = ttk.Frame(root2, padding=10)
    frm.grid()
    Button(frm, text="M1+", command=lambda: gameMode(),bd=5,bg="LIGHT GREEN", font=helv36).grid(column=0, row=0)
    Button(frm, text="M1-", command=lambda: gameMode(),bd=5,bg="LIGHT GREEN", font=helv36).grid(column=0, row=1)
    Button(frm, text="M2+", command=lambda: sensorMode(),bd=5,bg="LIGHT BLUE", font=helv36).grid(column=1, row=0)
    Button(frm, text="M2-", command=lambda: motorMode(),bd=5,bg = "YELLOW", font=helv36).grid(column=1, row=1)
    Button(frm, text="EXPERIMENTAL", command=lambda: experimental(),bd=5,bg = "PINK", font=helv36).grid(column=3, row=0)
    Button(frm, text="EXIT", command=root2.destroy,bd=5,bg = "GRAY").grid(column=4, row=1)
    root2.mainloop()
    #ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

def experimental():
    print("WARNING: Experimental mode...")
    
Button(frm, text="GAME CODE", command=lambda: gameMode(),width=27,height=25,bd=5,bg="LIGHT GREEN", font=helv36).grid(column=0, row=0)
Button(frm, text="SENSOR OUTPUT", command=lambda: sensorMode(),width=20,height=25,bd=5,bg="LIGHT BLUE", font=helv36).grid(column=1, row=0)
Button(frm, text="TEST MOTORS", command=lambda: motorMode(),width=20,height=25,bd=5,bg = "YELLOW", font=helv36).grid(column=2, row=0)
Button(frm, text="EXPERIMENTAL", command=lambda: experimental(),width=27,height=25,bd=5,bg = "PINK", font=helv36).grid(column=3, row=0)
Button(frm, text="EXIT", command=root.destroy,bd=5,bg = "GRAY").grid(column=0, row=1)
root.mainloop()



