import tkinter
import typing
from tkinter import *
from PIL import *
from PIL import ImageTk


class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config_app()

    def generate_auth(self, input: typing.List[dict]):
        self.entry_list: typing.List[tkinter.StringVar] = []
        count = len(input)

        img = Image.open('img/ddos-guard.jpg')
        render = ImageTk.PhotoImage(img)
        initil = Label(self, image=render)
        initil.image = render
        initil.pack()

        for i in range(count):
            self.entry_list.append(StringVar())
            Label(self, text=input[i].get('name')).grid(row=count + 1 + i, column=0)
            Entry(self, width=20, textvariable=self.entry_list[i], show='*' if input[i].get('is_password') else None).grid(row=count + 2 + i, column=0, padx=100)
            count += 1

        next_btn = Button(self, width=10, text='Далее', command=self.btn_next)
        next_btn.grid(
            row=1000, column=0, pady=20
        )
        self.mainloop()
        return self.btn_next()

    def btn_next(self):
        self.quit()
        return list(map(lambda x: x.get(), self.entry_list))


    def config_app(self):
        self.title('DdoS case')

        self.geometry('350x250+250+150')
        self.resizable(False, False)

if __name__ == '__main__':
    list = MainApp().generate_auth([{'name': 'number', 'is_password': False},
                                   {'name': 'пароль', 'is_password': True}])
    print(list)