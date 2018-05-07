
from tkinter import *

from PIL import ImageTk, Image
import os

import time
import random

def tstrength():
    canvas = Canvas(ResSys, width=800, height=800)
    canvas.pack()

    def onObjectClick(event):
        os.system('uu.py')

    def onObjectClick0(event):
        os.system('qq.py')

    def onObjectClick1(event):
        os.system('tt.py')

    def onObjectClick2(event):
        os.system('oo.py')

    def onObjectClick3(event):
        os.system('oo.py')

    def onObjectClick4(event):
        os.system('ss.py')

    def onObjectClickt1(event):
        os.system('uu.py')
    def onObjectClickt2(event):
        os.system('oo.py')
    def onObjectClickt3(event):
        os.system('ss.py')
    def onObjectClickt4(event):
        os.system('tt.py')
    def onObjectClick6(event):
        print('Got object click', event.x, event.y)
        window = Toplevel(ResSys)
        filename = PhotoImage(file = "mhh.gif")
        canv = Canvas(window, width=800, height=800)
        canv.pack()
        img = canv.create_image(20, 10, image=filename)

    def onObjectClick7(event):
        print('Got object click', event.x, event.y)
        window = Toplevel(ResSys)
        filename = PhotoImage(file = "mhh.gif")
        canv = Canvas(window, width=800, height=800)
        canv.pack()
        img = canv.create_image(20, 10, image=filename)

    ratio = 16
    vertical_edge_len = 5
    horizontal_edge_len = 12
    vertical = Frame(ResSys, bg='black', height=550, width=1)
    vertical.place(x=200, y=100)

    kt = canvas.create_text(440, 100, fill="darkblue", font=("Times 20 italic bold",12),
                             text="Temp range -900-950 deg cel      composition(wt%)=4.94%", tags="obj1Tag")
    at = canvas.create_text(440, 150, fill="darkblue", font=("Times 20 italic bold", 12),
                             text="Temp range -1487 deg cel      composition(wt%)=0.4005", tags="obj1Tag")
    tt = canvas.create_text(540, 370, fill="darkblue", font=("Times 20 italic bold", 12),
                             text="Temp range -1487 deg cel", tags="obj1Tag")
    tt2 = canvas.create_text(540, 420, fill="darkblue", font=("Times 20 italic bold", 12),
                             text="composition(wt%)=26.53%", tags="obj1Tag")
    horizontal = Frame(ResSys, bg='blue', height=1,
                       width=50)
    horizontal.place(x=200, y=150)

    horizontal2 = Frame(ResSys, bg='blue', height=1,
                        width=50)
    horizontal2.place(x=200, y=200)

    horizontal3 = Frame(ResSys, bg='blue', height=1,
                        width=50)
    horizontal3.place(x=200, y=250)

    horizontal4 = Frame(ResSys, bg='blue', height=1,
                        width=50)
    horizontal4.place(x=200, y=300)

    horizontal5 = Frame(ResSys, bg='blue', height=1,
                        width=50)
    horizontal5.place(x=200, y=560)

    horizontal6 = Frame(ResSys, bg='blue', height=1,
                        width=50)
    horizontal6.place(x=200, y=350)

    horizontal7 = Frame(ResSys, bg='blue', height=1,
                        width=50)
    horizontal7.place(x=200, y=450)

    horizontal8 = Frame(ResSys, bg='blue', height=1,
                        width=50)
    horizontal8.place(x=200, y=610)

    ss1= canvas.create_text(200, 100, fill="darkblue", font="Times 20 italic bold",
                            text="K2O",tags="obj1Tag")
    ss=canvas.create_text(200, 150, fill="darkblue", font="Times 20 italic bold",
                       text="Al2O3")
    ss2 = canvas.create_text(200,200, fill="darkblue", font="Times 20 italic bold",
                            text="Na2O")
    nat = canvas.create_text(440, 200, fill="darkblue", font=("Times 20 italic bold", 12),
                             text="Temp range -1300 deg cel      composition(wt%)=1.8%", tags="obj1Tag")
    ss3 = canvas.create_text(200, 250, fill="darkblue", font="Times 20 italic bold",
                            text="MgO")
    mt = canvas.create_text(460, 250, fill="darkblue", font=("Times 20 italic bold", 12),
                             text="Temp range -1400-1500 deg cel      composition(wt%)=7.33%", tags="obj1Tag")
    ss4= canvas.create_text(200, 300, fill="darkblue", font="Times 20 italic bold",
                            text="FeO")
    ft = canvas.create_text(460, 300, fill="darkblue", font=("Times 20 italic bold", 12),
                             text="Temp range -1400-1500 deg cel      composition(wt%)=7.33%", tags="obj1Tag")
    ss5= canvas.create_text(200, 560, fill="darkblue", font="Times 20 italic bold",
                            text="SiO2")
    st = canvas.create_text(450, 560, fill="darkblue", font=("Times 20 italic bold", 12),
                             text="Temp range -1487 deg cel      composition(wt%)=2.789", tags="obj1Tag")
    ss6= canvas.create_text(200, 400, fill="darkblue", font="Times 20 italic bold",
                            text="TiO2")
    tio2g1 = canvas.create_text(380, 330, fill="darkblue", font="Times 20 italic bold",
                             text="Graph 1")
    tio2g2 = canvas.create_text(380, 360, fill="darkblue", font="Times 20 italic bold",
                             text="Graph 2")
    tio2g3 = canvas.create_text(380, 400, fill="darkblue", font="Times 20 italic bold",
                             text="Graph 3")
    tio2g4 = canvas.create_text(380, 440, fill="darkblue", font="Times 20 italic bold",
                             text="Graph 4")
    tio2g5 = canvas.create_text(380, 470, fill="darkblue", font="Times 20 italic bold",
                                text="Graph 5")
    ss7= canvas.create_text(200, 510, fill="darkblue", font="Times 20 italic bold",
                            text="ZrO2")
    zt = canvas.create_text(470, 510, fill="darkblue", font=("Times 20 italic bold", 12),
                             text="Temp range -1400-1500 deg cel      composition(wt%)=4.25%", tags="obj1Tag")
    line =canvas.create_line(240,390,330,330)
    line2 = canvas.create_line(240, 395, 330, 360)
    line3= canvas.create_line(240, 400, 330, 400)
    line4= canvas.create_line(240, 405, 330, 440)
    line5 = canvas.create_line(240, 410, 330, 470)
    canvas.tag_bind(ss1,'<ButtonPress-1>',onObjectClick)
    canvas.tag_bind(ss2, '<ButtonPress-1>', onObjectClick1)
    canvas.tag_bind(ss3, '<ButtonPress-1>', onObjectClick2)
    canvas.tag_bind(ss4, '<ButtonPress-1>', onObjectClick3)
    canvas.tag_bind(ss5,'<ButtonPress-1>',onObjectClick4)
    canvas.tag_bind(tio2g1, '<ButtonPress-1>', onObjectClickt1)
    canvas.tag_bind(tio2g2, '<ButtonPress-1>', onObjectClickt2)
    canvas.tag_bind(tio2g3, '<ButtonPress-1>', onObjectClickt3)
    canvas.tag_bind(tio2g4, '<ButtonPress-1>', onObjectClickt4)
    canvas.tag_bind(tio2g5, '<ButtonPress-1>', onObjectClick0)
    canvas.tag_bind(ss7, '<ButtonPress-1>', onObjectClick0)
    canvas.tag_bind(ss, '<ButtonPress-1>', onObjectClick4)


ResSys = Tk()
ResSys.geometry("1000x700+0+0")
ResSys.title("Tensile Strength Calculation")




b1 = Button(ResSys, text="Load Material is fun", command=tstrength)
main = Label(ResSys, font=('25'), text="File Loading", fg='BLUE')
main.pack()

b1.pack()

ResSys.mainloop()
