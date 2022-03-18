import typing
from tkinter import *


class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config_app()

    def generate_auth(self, input: typing.List[dict]) -> typing.List[str]:
        self.list = []
        count = len(input)

        for i in range(count):
            self.list.append(0)
            self.list[i] = StringVar()
            Label(self, text=input[i].get('name')).grid(row=count + 1 + i, column=0)
            Entry(self, width=20).grid(
                row=count + 2 + i, column=0, padx=100
            )
            count += 1

        next_btn = Button(self, width=10, text='Далее')
        next_btn.grid(
            row=1000, column=0, pady=20
        )

        self.mainloop()

    def btn_next(self):
        pass

    def config_app(self):
        self.title('DdoS case')
        self.geometry('350x250+250+150')
        self.resizable(False, False)


if __name__ == '__main__':
    MainApp().generate_auth([{'name': 'number', 'is_password': False},
                             {'name': 'пароль', 'is_password': True}])
