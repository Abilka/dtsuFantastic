from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('DDoS-Guard')
        self.resizable(False, False)
        self.config(background='#F0F0F0') #F0F0F0
        self.iconphoto(True, PhotoImage(file='img/DDoS-Guard.png'))
        self.geometry('700x590+150+150') #1000x590+150+150

        img = Image.open('img/ddos.png') #685x458
        render = ImageTk.PhotoImage(img)
        initil = Label(self, image=render)
        initil.image = render
        initil.grid()

        #вывел текст без стилей
        '''l1 = Label(self, text='Добро пожаловать в DDoS-Guard!', font=('Open Sans', 20), foreground='#2F9AE1', background='#F0F0F0').grid(
            row=2, column=0, pady=20
        )'''
        #со стилями
        style = Style()
        style.configure('BW.TLabel', foreground='#2F9AE1', background='#F0F0F0')
        l1 = Label(text='Добро пожаловать в DDoS-Guard!', style='BW.TLabel', font=('Open Sans', 20)).grid(
            row=2, column=0, pady=20
        )

if __name__ == '__main__':
    App().mainloop()