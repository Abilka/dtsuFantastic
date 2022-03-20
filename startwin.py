from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setting_win()

    def setting_win(self):
        self.title('DDoS-Guard')
        self.geometry('690x400+150+150')
        self.iconphoto(True, PhotoImage(file='img/DDoS-Guard_logo.svg.png'))
        self.resizable(False, False)

        img = Image.open('img/bg.jpg')
        idraw = ImageDraw.Draw(img)
        text = 'Добро пожаловать в систему!\n\nПройдите авторизацию для продолжения использования системы'
        font = ImageFont.truetype('arial.ttf', size=16)
        idraw.text((160, 160), text, font=font)
        render = ImageTk.PhotoImage(img)
        initil = Label(self, image=render)
        initil.image = render
        initil.grid()

        Button(self, text='Далее', width=10, height=1, font=("Arial Bold", 10), bg='white').grid(
            row=0, column=0, pady=(160, 0), padx=(0, 650)
        )

if __name__ == '__main__':
    App().mainloop()