# Imports
from tkinter import *

class App:
    def mb_one_down(self, event):
        self.mb_one = True
    def mb_one_up(self, event):
        self.mb_one = False
    def mb_motion(self, event):
        self.m_x, self.m_y = event.x, event.y
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
        # Setup control for left click on canvas
        self.mb_one = False
        self.m_x = 0
        self.m_y = 0
        # Binds
        self.canvas.bind("<Button-1>", self.mb_one_down)
        self.canvas.bind('<ButtonRelease-1>', self.mb_one_up)
        self.canvas.bind('<Motion>', self.mb_motion)
    def custom_update(self):
        if (self.mb_one):
            self.m_image.put('black', (self.m_x, self.m_y))
    def custom_main_loop(self):
        while True:
            self.custom_update()
            self.root.update_idletasks()
            self.root.update()
            
app = App()
app.custom_main_loop()