from tkinter import *
from PIL import Image, ImageTk


class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setting()
        self.bind('<Return>', self.exit_window)

        img = Image.open('img/error.png')
        img = img.resize((75, 75), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(img)
        initil = Label(self, image=render, bg='#fff')
        initil.image = render
        initil.grid(row=0, column=0, padx=110, pady=10)

        Label(self, text='Введённые данные не прошли проверку.\nПовторите попытку на новой строке',
              bg='#fff', fg='#000'). \
            grid(row=1, column=0)

        self.btn = Button(self, text='OK', bg='#fff', fg='#000', command=lambda: self.destroy(), width=10)
        self.btn.grid(
            row=2, column=0, pady=20, padx=20
        )
        self.mainloop()

    def exit_window(self, event):
        self.destroy()

    def setting(self):
        self.geometry('300x250+450+200')
        self.title('Ошибка')
        self.config(bg='#fff')
        self.resizable(False, False)
        self.iconphoto(False, PhotoImage(file='img/DDoS-Guard_logo.svg.png'))
