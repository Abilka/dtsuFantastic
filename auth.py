import typing
from tkinter import *


class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config_app()

    def generate_auth(self, input: typing.List[dict]) -> typing.List[str]:
        for par in input:
            Label(self, text=par['name']).grid(
                row=2, column=2
            )

            login_entry = Entry(self, width=20)
            login_entry.grid(
                row=3, column=2
            )

        #
        # # Label(self, text='Введите пароль').grid(
        # #     row=5, column=2
        # # )
        # password_entry = Entry(self, width=20, show='*')
        # password_entry.grid(
        #     row=6, column=2
        # )
        #
        # next_btn = Button(self, text='Далее', width=10, command=self.btn_next)
        # next_btn.grid(
        #     row=8, column=2
        # )

        self.mainloop()

    def btn_next(self):
        pass

    def config_app(self):
        self.title('DdoS case')
        self.geometry('350x250+250+150')
        self.resizable(False, False)


if __name__ == '__main__':
    MainApp().generate_auth([{'name': 'пароль', 'is_password': True}])
