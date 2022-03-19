import tkinter
import typing
from tkinter import *
import auth_method
from PIL import Image, ImageTk
from tkinter import messagebox


class MainApp:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = Tk()
        self.config_app()

    def error_window(self):
        self.message = Toplevel()
        # messagebox.showerror('Ошибка', 'Введённые данные не прошли проверку.\nПовторите попытку на новой строке')
        self.message.geometry('300x200+600+300')
        self.message.title('Ошибка')
        self.message.config(bg='#fff')
        self.message.resizable(False, False)
        self.message.iconphoto(False, PhotoImage(file='img/DDoS-Guard_logo.svg.png'))

        img = Image.open('img/error.png')
        img = img.resize((75, 75), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(img)
        initil = Label(self.message, image=render, bg='#fff')
        initil.image = render
        initil.grid(row=0, column=0, padx=110, pady=10)

        Label(self.message, text='Введённые данные не прошли проверку.\nПовторите попытку на новой строке',
              bg='#fff', fg='#000'). \
            grid(row=1, column=0)

        self.btn = Button(self.message, text='OK', bg='#fff', fg='#000', command=lambda: self.message.destroy())
        self.btn.grid(
            row=2, column=0, pady=20, padx=20
        )

    def generate_auth(self, input: typing.List[auth_method.Input], service: str):
        self.entry_list: typing.List[tkinter.StringVar] = []
        count = len(input)

        # Сервис
        self.service = Label(self.root, text=service, bg='#fff', font=14, fg='#347aeb')
        self.service.grid(row=1, column=0, pady=(10, 10))

        for i in range(count):
            self.entry_list.append(StringVar())
            Label(self.root, text=input[i].name, bg='#fff', fg='#000').grid(row=count + 1 + i, column=0, pady=3)
            Entry(self.root, width=20, textvariable=self.entry_list[i], show='*' if input[i].is_hide else None,
                  bg='#fff', fg='#000').grid(row=count + 2 + i, column=0, padx=100)
            count += 1

        next_btn = Button(self.root, width=10, text='Далее', command=self.root.quit, bg='#fff', fg='#000')
        next_btn.grid(
            row=1000, column=0, pady=20
        )

        self.img = PhotoImage(file='img/DDoS-Guard_logo.svg.png', master=self.root)
        bg_logo = Label(self.root, image=self.img, bg='#fff')
        bg_logo.grid(row=0, column=0, pady=10)

        self.root.mainloop()
        self.root.destroy()
        return self.btn_next()

    def btn_next(self):
        self.root.quit()
        return list(map(lambda x: x.get(), self.entry_list))

    def config_app(self):
        self.root.title('DDoS case')
        self.root.config(bg='#fff')
        self.root.geometry('330x350+450+200')
        self.root.iconphoto(False, PhotoImage(file='img/DDoS-Guard_logo.svg.png', master=self.root))
        self.root.resizable(False, False)
