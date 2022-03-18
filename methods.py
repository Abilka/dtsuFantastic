import sqlite3


class Check:
    def __init__(self):
        ...

    def standart(self, login: str, password: str) -> bool:

        return True


    def vk(self, number: str or int, password: str) -> bool:
        import vk_api
        vk = vk_api.VkApi(login=number, password=password)
        try:
            vk.auth()
        except vk_api.BadPassword:
            return False
        except vk_api.TwoFactorError:
            return True
        except vk_api.AuthError:
            return True

    def telegram(self, number: str) -> bool:
        ...

    def totp(self, salt: str, code: str or int) -> bool:
        import pyotp

        code = str(code)
        totp = pyotp.TOTP(salt)
        if code == str(totp.now()):
            return True
        else:
            return False


class DB:
    def __init__(self):
        self.con = sqlite3.connect("base.db")
        self.cur = self.con.cursor()

    def get_login_paasord(self, login: str, password: str) -> bool:
        self.cur.execute('SELECT id WHERE login=? AND password=?')
