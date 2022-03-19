from tkinter import *
from PIL import Image, ImageTk

class windower(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry('420x250+550+350')
        self.config(background='white')
        self.title('Ошибка')
        self.iconphoto(True, PhotoImage(file='img/error.png'))
        self.resizable(False, False)

        img = Image.open('img/error.png')
        img = img.resize((75, 75), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(img)
        initil = Label(self, image=render, bg='#fff')
        initil.image = render
        initil.grid(row=0, column=0, pady=(10, 70), padx=(55, 10))

        text = 'Ошибка!\n\nНеправильный логин или пароль.'
        l1 = Label(self, text=text, font=('Arial Bold', 15), bg='white').grid(
            row=0, column=0, pady=(90, 20), padx=(55, 10)
        )

        btn = Button(self, text='Далее', font=('Arial Bold', 13), pady='8', padx='20', command=self.quit).grid(
            row=1, column=0, pady=(5, 5), padx=(55, 10)
        )


if __name__ == '__main__':
    windower().mainloop()
