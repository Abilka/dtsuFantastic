
import auth
import auth_method
import auth_success
import error_window
from tkinter import *

import startwin

if __name__ == '__main__':
    startwin.App()
    for service in auth_method.auth_method:
        root = auth.MainApp()
        result = root.generate_auth(service.inputs, service.name, service.is_skip)


        while service.func_check(*result) is not True and not (result[0] == '' and service.is_skip):
            error_window.MainApp()

            root = auth.MainApp()
            result = root.generate_auth(service.inputs, service.name, service.is_skip)
        auth_success.MainApp()
