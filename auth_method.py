from main import *

auth_method = [
    [AuthMethod('VK', [Input('Логин'), Input("Пароль", True)])],
    [AuthMethod('GitHub', [Input('Логин'), Input('Пароль', True)])],
    [AuthMethod('Google', [Input('Логин'), Input('Пароль', True)])],
    [AuthMethod('Telegram', [Input('Номер')])],
]