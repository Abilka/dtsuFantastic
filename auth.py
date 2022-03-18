import tkinter
import typing
from tkinter import *
from tkinter import ttk

import PIL.Image
from PIL import *
from PIL import ImageTk

import auth_method


class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config_app()

    def generate_auth(self, input: typing.List[auth_method.Input]):
        self.entry_list: typing.List[tkinter.StringVar] = []
        count = len(input)
        for i in range(count):
            self.entry_list.append(StringVar())
            Label(self, text=input[i].name).grid(row=count + 1 + i, column=0)
            Entry(self, width=20, textvariable=self.entry_list[i], show='*' if input[i].is_hide else None).grid(
                row=count + 2 + i, column=0, padx=100)
            count += 1

        next_btn = Button(self, width=10, text='Далее', command=self.btn_next)
        next_btn.grid(
            row=1000, column=0, pady=20
        )

        img = ImageTk.PhotoImage(Image.open('img/-GlkRC8TPVo.jpg'))
        b = Label(self, image=img)
        b.grid()

        # img = PhotoImage(file='img/-GlkRC8TPVo.jpg')
        # self.bg = ttk.Label(self)
        # self.bg['image'] = img
        # self.bg.grid()

        self.mainloop()
        return self.btn_next()

    def btn_next(self):
        self.quit()
        return list(map(lambda x: x.get(), self.entry_list))

    def config_app(self):
        self.title('DdoS case')
        self.config(bg='#fff')
        self.geometry('350x250+250+150')
        # self.resizable(False, False)


if __name__ == '__main__':
    list = MainApp().generate_auth(auth_method.auth_method[0].inputs)
    # print()
    print(list)
