import typing

class Input:
    def __init__(self, name: str, is_password: bool=False):
        self.name = name
        self.is_hide = is_password

class AuthMethod:
    def __init__(self, name: str, input_list: typing.List[Input]):
        self.name = name
        self.inputs = input_list

auth_method = [
    [AuthMethod('VK', [Input('Логин'), Input("Пароль", True)])],
    [AuthMethod('GitHub', [Input('Логин'), Input('Пароль', True)])],
    [AuthMethod('Google', [Input('Логин'), Input('Пароль', True)])],
    [AuthMethod('Telegram', [Input('Номер')])],
]
print(auth_method)

