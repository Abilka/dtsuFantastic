import tkinter
import typing
from tkinter import *

import auth_method




class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_app()

    def __enter__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_app()
        return self

    def generate_auth(self, input: typing.List[auth_method.Input], service: str):
        self.entry_list: typing.List[tkinter.StringVar] = []
        count = len(input)

        # Сервис
        self.service = Label(self, text=service, bg='#fff', font=14, fg='#347aeb')
        self.service.grid(row=1, column=0, pady=(10, 10))

        for i in range(count):
            self.entry_list.append(StringVar())
            Label(self, text=input[i].name, bg='#fff', fg='#000').grid(row=count + 1 + i, column=0, pady=3)
            Entry(self, width=20, textvariable=self.entry_list[i], show='*' if input[i].is_hide else None,
                  bg='#fff', fg='#000').grid(row=count + 2 + i, column=0, padx=100)
            count += 1

        next_btn = Button(self, width=10, text='Далее', command=self.btn_next, bg='#fff', fg='#000')
        next_btn.grid(
            row=1000, column=0, pady=20
        )

        self.img = PhotoImage(file='img/DDoS-Guard_logo.svg.png', master=self)
        bg_logo = Label(self, image=self.img, bg='#fff')
        bg_logo.grid(row=0, column=0, pady=10)

        self.mainloop()
        self.destroy()
        return self.btn_next()

    def btn_next(self):
        self.quit()
        return list(map(lambda x: x.get(), self.entry_list))

    def config_app(self):
        self.title('DDoS case')
        self.config(bg='#fff')
        self.geometry('330x350+450+200')
        self.iconphoto(False, PhotoImage(file='img/DDoS-Guard_logo.svg.png'))
        self.resizable(False, False)
