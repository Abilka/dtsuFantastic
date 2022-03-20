import typing

import methods


class Input:
    def __init__(self, name: str, is_password: bool = False):
        self.name = name
        self.is_hide = is_password


class AuthMethod:
    def __init__(self, name: str, input_list: typing.List[Input], func_check, skip=False):
        self.name = name
        self.inputs = input_list
        self.func_check = func_check
        self.is_skip = skip

    def is_valid(self) -> bool:
        return self.func_check()


auth_method = [

    AuthMethod('Стандартная авторизация', [Input('Логин'), Input("Пароль", True)], methods.Check().standart),
    AuthMethod('Pincode', [Input('Код')], methods.Check().pin),
    AuthMethod('Google Auth', [Input('Код из приложения')], methods.Check().totp),
    AuthMethod('ВКонтакте', [Input('Логин'), Input("Пароль", True)], methods.Check().vk),
    AuthMethod('Apple ID', [Input('Логин'), Input("Пароль", True)], methods.Check().apple_id),
    AuthMethod('GitHub', [Input('Логин'), Input("Пароль", True)], methods.Check().github),
    AuthMethod('Sber', [Input('Логин'), Input("Пароль", True)], methods.Check().sber, True),
    AuthMethod('GosUslugi', [Input('Логин'), Input("Пароль", True)], methods.Check().gosuslugi),
    AuthMethod('СНИЛС', [Input('СНИЛС')], methods.Check().snils, True),

    # AuthMethod('Steam', [Input('Логин'), Input("Пароль", True)], methods.Check().steam, True),

    # AuthMethod('Google', [Input('Логин'), Input('Пароль', True)]),
    # AuthMethod('Telegram', [Input('Номер')]),
]
