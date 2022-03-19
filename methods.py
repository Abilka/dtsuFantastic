import sqlite3
import requests

class User:
    def __init__(self, id: str or int=None):
        self.id = id

user: User = User()


class Check:
    def __init__(self):
        ...

    def standart(self, login: str, password: str) -> bool:
        return True

    def google(self, login: str, password: str) -> bool:

        return True

    def pin(self, pincode: str or int) -> bool:
        return True

    def wikipedia(self, login: str, password: str) -> bool:
        import requests
        headers = {
            'authority': 'ru.wikipedia.org',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'upgrade-insecure-requests': '1',
            'origin': 'https://ru.wikipedia.org',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://ru.wikipedia.org/w/index.php?title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%92%D1%85%D0%BE%D0%B4&returnto=%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F+%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'WMF-Last-Access=19-Mar-2022; WMF-Last-Access-Global=19-Mar-2022; GeoIP=RU:ROS:Rostov-on-Don:47.24:39.72:v4; ruwikimwuser-sessionId=e22c6dcb76f8762e4a48; ruwikiss0-UserName=VaineBa; ruwikiUserName=VaineBa; ruwiki-mw-tour=%7B%22version%22%3A1%2C%22tours%22%3A%7B%7D%7D; ruwikigrowth.welcomesurvey.phase=logged_out; loginnotify_prevlogins=2022-gnrmc1-qhe8cl8hbm1j5isu4jl1vygw67reije; ruwikiwmE-sessionTickLastTickTime=1647687943741; ruwikiwmE-sessionTickTickCount=23; ruwikiel-sessionId=d34dcb7a1001e0d0c4d6; ss0-ruwikiSession=tjl02em4efq632hdvhja74iuhgoj4btc; ruwikiSession=tjl02em4efq632hdvhja74iuhgoj4btc; cpPosIndex=2%401647687952%23a52495f3fe4fa98d5f20fab1c3649b90; UseDC=master; UseCDNCache=false',
        }

        params = (
            ('title', '\u0421\u043B\u0443\u0436\u0435\u0431\u043D\u0430\u044F:\u0412\u0445\u043E\u0434'),
            ('returnto',
             '\u0417\u0430\u0433\u043B\u0430\u0432\u043D\u0430\u044F \u0441\u0442\u0440\u0430\u043D\u0438\u0446\u0430'),
        )

        data = {
            'wpName': login,
            'wpPassword': password,
            'wploginattempt': '\u0412\u043E\u0439\u0442\u0438',
            'wpEditToken': '+\\',
            'title': '\u0421\u043B\u0443\u0436\u0435\u0431\u043D\u0430\u044F:\u0412\u0445\u043E\u0434',
            'authAction': 'login',
            'force': '',
            'wpLoginToken': '5128bf1a77d4482582183d02fb9ee7c56235b910+\\',
            'geEnabled': '-1',
            'geNewLandingHtml': '-1'
        }

        response = requests.post('https://ru.wikipedia.org/w/index.php', headers=headers, params=params, data=data)


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
        return False


class DB:
    def __init__(self):
        self.con = sqlite3.connect("base.db")
        self.cur = self.con.cursor()

    def get_login_password(self, login: str, password: str) -> bool:
        result = self.cur.execute('SELECT id FROM user WHERE login=? AND password=?', (login, password)).fetchone()
        if result is not None:
            user.id = result[0]
            return True
        return False

    def get_pincode(self, pincode: str or int) -> bool:
        result = self.cur.execute('SELECT pincode FROM user WHERE id=?', (user.id,)).fetchone()
        if result is not None and result[0] == pincode:
            return True
        return False