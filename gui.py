
import tkinter
import math
import random

class meter(tkinter.Canvas):
    def __init__(self,parent,bg,height,width):
        super().__init__(master=parent,bg=bg,height=height,width=width)
        self.minimum = 0
        self.maximum = 100
        self.value = 0

    def refresh(self):
        if self.maximum>0:angle = (180/self.maximum)*self.value
        else:angle = 180
        length = 140
        x2 = 175-math.cos(math.pi * angle/180) * length
        y2 = 170-math.sin(math.pi * angle/180) * length
        x3 = 175-math.cos(math.pi * angle/180) * (length - 50)
        y3 = 170-math.sin(math.pi * angle/180) * (length - 50)
        self.delete('all')
        arc = self.create_arc((21,20,329,320),start=0, extent = 180,fill='#02d402')
        arc1 = self.create_arc((21,20,329,320),start=0, extent = 140,fill='#00FF00',outline='')
        arc2 = self.create_arc((21,20,329,320),start=0, extent = 100,fill='#c3ff42',outline='')
        arc3 = self.create_arc((21,20,329,320),start=0, extent = 60,fill='#ffff00',outline='')
        arc4 = self.create_arc((21,20,329,320),start=0, extent = 20,fill='#ffe000',outline='')
        blind = self.create_arc((71,70,279,270),start=0, extent = 180,fill='#ffffff')
        mintext = self.create_text(10, 180, text=str(self.minimum), fill='black', font=('Helvetica 15 bold'))
        maxtext = self.create_text(330, 180, text=str(self.maximum), fill='black', font=('Helvetica 15 bold'))
        needle = self.create_line(175,170,x2,y2, fill="#ff0000", width=5)
        needle = self.create_line(175,170,x3,y3, fill="#ff0000", width=10)
        blind2 = self.create_oval((141,140,209,200),fill='#dd0000')
        

    def setvalue(self,value,minval=0,maxval=100):
        self.minimum = minval
        self.maximum = maxval
        self.value = value
        self.refresh()
        

class gui:
    def __init__(self, app):
        self.app = app
        self.app.geometry('500x350')
        self.draw()
        self.app.mainloop()

    def draw(self):
        for i in range(3):
            x = meter(self.app,bg="white", height=200,width=350)
            x.setvalue(random.choice(list(range(100))))
            x.pack(side=tkinter.LEFT)


if __name__ == '__main__':
    gui(tkinter.Tk())
