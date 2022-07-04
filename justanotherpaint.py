# Imports
from tkinter import *
from tkinter import colorchooser
import math
import time

class App:
    def color_button_press(self):
        color_tuple = colorchooser.askcolor(title="Please pick a color...")
        self.selected_color = color_tuple[1]
    def mb_one_down(self, event):
        self.mb_one = True
    def mb_one_up(self, event):
        self.mb_one = False
    def mb_motion(self, event):
        self.m_x, self.m_y = event.x, event.y
    def mb_update(self):
        self.m_x_c = self.m_x
        self.m_y_c = self.m_y
        if (self.mb_one):
            self.paint_line(self.m_x_p, self.m_y_p, self.m_x_c, self.m_y_c)
        self.m_x_p = self.m_x_c
        self.m_y_p = self.m_y_c
    def __init__(self):
        # Setup the window
        self.root = Tk()
        self.root.title('Just another drawing app')
        self.root.geometry('640x480')
        self.root.resizable(False,False)
        # Set up canvas
        self.canvas = Canvas(self.root, width=320, height=240)
        self.canvas.pack()
        # Set up image in memory
        self.m_image = PhotoImage(width=320, height=240)
        self.m_image.put('white', to=(0, 0, 320, 240))
        # Display image on canvas
        self.canvas.create_image(0,0,anchor=NW,image=self.m_image)
        # Create the color button
        self.selected_color = 'black'
        self.color_button = Button(self.root, text="Pick Color", command=self.color_button_press)
        self.color_button.pack()
        # Create the sleep check box
        self.sleep_var = IntVar()
        self.sleep_check = Checkbutton(self.root, text="Sleep between frames", variable=self.sleep_var, onvalue=1, offvalue=0)
        self.sleep_check.pack()
        # Setup control for left click on canvas
        self.mb_one = False
        self.m_x = 0
        self.m_y = 0
        self.m_x_c = 0
        self.m_y_c = 0
        self.m_x_p = 0
        self.m_y_p = 0
        # Binds
        self.canvas.bind("<Button-1>", self.mb_one_down)
        self.canvas.bind('<ButtonRelease-1>', self.mb_one_up)
        self.canvas.bind('<Motion>', self.mb_motion)
    def custom_main_loop(self):
        while True:
            self.mb_update()
            self.root.update_idletasks()
            self.root.update()
            if self.sleep_var.get() == 1:
                time.sleep(0.01)
    def safeput(self, ix, iy):
        tempx = int(ix)
        tempy = int(iy)
        if (tempx >= 0 & tempy >= 0 & tempx <= 320 & tempy <= 240):
            self.m_image.put(self.selected_color, (int(tempx),int(tempy)) )
    def paint_line(self, x1, y1, x2, y2):
        tempx = x1
        xdir = math.copysign(1, x2-x1)
        tempy = y1
        ydir = math.copysign(1, y2-y1)
        while ( (not tempx == x2)|(not tempy == y2) ):
            self.safeput(tempx, tempy)
            if (not tempx == x2):
                tempx += xdir
            if (not tempy == y2):
                tempy += ydir
            
app = App()
app.custom_main_loop()