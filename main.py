import typing


class Input:
    def __init__(self, name: str, is_password: bool = False):
        self.name = name
        self.is_hide = is_password


class AuthMethod:
    def __init__(self, name: str, input_list: typing.List[Input]):
        ...


if __name__ == '__main__':
    pass
