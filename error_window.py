from tkinter import *
from PIL import Image, ImageTk


class MainApp(Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setting()

        img = Image.open('img/error.png')
        img = img.resize((75, 75), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(img)
        initil = Label(self, image=render, bg='#fff')
        initil.image = render
        initil.grid(row=0, column=0, padx=110, pady=10)

        Label(self, text='Введённые данные не прошли проверку.\nПовторите попытку на новой строке',
              bg='#fff'). \
            grid(row=1, column=0)

        self.btn = Button(self, text='OK', bg='#fff', command=lambda: self.destroy())
        self.btn.grid(
            row=2, column=0, pady=20, padx=20
        )

    def setting(self):
        self.geometry('300x200')
        self.title('Ошибка')
        self.config(bg='#fff')
        self.resizable(False, False)
        self.iconphoto(False, PhotoImage(file='img/DDoS-Guard_logo.svg.png'))


if __name__ == '__main__':
    MainApp().mainloop()
