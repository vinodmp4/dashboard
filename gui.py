
import tkinter
import math
import random

class meter(tkinter.Canvas):
    def __init__(self,parent,bg,height,width):
        super().__init__(master=parent,bg=bg,height=height,width=width)
        self.width = width
        self.height = height
        self.minimum = 0
        self.maximum = 100
        self.value = 0
        self.padding = int(self.width/20)
        

    def refresh(self):
        if self.maximum>0:angle = (180/self.maximum)*self.value
        else:angle = 180
        length = self.padding*8
        x2 = int(self.width/2)-math.cos(math.pi * angle/180) * length
        y2 = (self.height-self.padding*3)-math.sin(math.pi * angle/180) * length
        x3 = int(self.width/2)-math.cos(math.pi * angle/180) * (length - 50)
        y3 = (self.height-self.padding*3)-math.sin(math.pi * angle/180) * (length - 50)
        self.delete('all')
        arc_area = (self.padding,self.padding,self.width-self.padding,self.height+self.padding*6)
        blind1 = (self.padding*3,self.padding*3,self.width-self.padding*3,self.height+self.padding*4)
        areas = (arc_area,arc_area,arc_area,arc_area,arc_area,blind1)
        extend_values = (180,140,100,60,20,180);colours = ('#02d402','#00FF00','#c3ff42','#ffff00','#ffe000','#ffffff')
        for e, c, a in zip(extend_values,colours,areas):
            self.create_arc(a,start=0, extent = e,fill=c, outline='')
        mintext = self.create_text(self.padding, self.height-self.padding*2, text=str(self.minimum), fill='black', font=('Helvetica 15 bold'))
        maxtext = self.create_text(self.width-self.padding, self.height-self.padding*2, text=str(self.maximum), fill='black', font=('Helvetica 15 bold'))
        needle = self.create_line(int((self.width)/2),self.height-self.padding*3,x2,y2, fill="#ff0000", width=5)
        needle = self.create_line(int((self.width)/2),self.height-self.padding*3,x3,y3, fill="#ff0000", width=10)
        blind2 = self.create_oval((((self.width)/2)-self.padding,(self.height-self.padding*3)-self.padding,((self.width)/2)+self.padding,
                                   (self.height-self.padding*3)+self.padding),fill='#dd0000')
        

    def setvalue(self,value,minval=0,maxval=100):
        self.minimum = minval
        self.maximum = maxval
        self.value = value
        self.refresh()
        

class gui:
    def __init__(self, app):
        self.app = app
        self.app.geometry('1200x250')
        self.draw()
        self.app.mainloop()

    def draw(self):
        for i in range(3):
            x = meter(self.app,bg="white", height=250,width=400)
            x.setvalue(random.choice(list(range(100))))
            x.pack(side=tkinter.LEFT)

    


if __name__ == '__main__':
    gui(tkinter.Tk())
