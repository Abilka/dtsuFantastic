import sqlite3
import requests
import bs4
class User:
    def __init__(self, id: str or int=None):
        self.id = id
        self.salt = None
        self.number = None

user: User = User()


class Check:
    def __init__(self):
        ...

    def standart(self, login: str, password: str) -> bool:
        return DB().get_login_password(login, password)

    def github(self, login: str, password: str) -> bool:
        headers = {
            'authority': 'github.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'upgrade-insecure-requests': '1',
            'origin': 'https://github.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '_device_id=75bf69a06671899179c5f58a6cb8eb79; _octo=GH1.1.35382506.1647661301; tz=Europe%2FMoscow; tz=Europe%2FMoscow; color_mode=%7B%22color_mode%22%3A%22dark%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark_dimmed%22%2C%22color_mode%22%3A%22dark%22%7D%7D; has_recent_activity=1; logged_in=no; _gh_sess=kGN2g8uY9Zya2gGIje0eAAKa1v14PHC79RefJKHDx6m0OIl8j1oLKtV3tEYEEFoJfN4RoENhvec6fysM3i4DMQmN9%2FBLL7UuQbSkPmJ3RJDC0v0RDaHsM1%2BF8FhVUTuTCA5DwKjQRmAVFc5zHIh19QG5yVAvbvj5hJHz%2Bv07hmM7Nw4KoyE0ENpVtY6%2Bnhv2Qei1nK%2FIPZSL1IRy6qW1HvmddVI1jFU%2FlGvoHoYwcQK3baxwySvBWJ5E%2BWmVPrGNgX2KpoyoghhZNx4t20%2B9DA%3D%3D--vPsLT%2BP4VlsCuP50--8B52ROw53YdL%2BgkF33vosw%3D%3D',
        }

        data = {
            'commit': 'Sign in',
            'authenticity_token': '4xcNbTKLLFlzvIUo45vWJHD8zU6AOCal45SKvKjuf1UMrcAytZdKmP_hYeE3q0mOuj-lBWqfzKR-JX2PVuO7jg',
            'login': login,
            'password': password,
            'trusted_device': '',
            'webauthn-support': 'supported',
            'webauthn-iuvpaa-support': 'supported',
            'return_to': 'https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home',
            'allow_signup': '',
            'client_id': '',
            'integration': '',
            'required_field_6d0b': '',
            'timestamp': '1647717531070',
            'timestamp_secret': '759bcc7fc137ed3ff77508e5a8d722626eef6fa984278a372b841771d09a6b54'
        }

        response = requests.post('https://github.com/session', headers=headers, data=data)
        if 'Incorrect username or password.' in response.text:
            return False
        return True

    def pin(self, pincode: str or int) -> bool:
        return DB().get_pincode(str(pincode))

    def apple_id(self, login: str, password: str) -> bool:
        login = "+"+login if '+' not in login else login
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

    def vk(self, login: str or int, password: str) -> bool:
        import vk_api
        login = "+"+login if '+' not in login else login
        vk = vk_api.VkApi(login=login, password=password)
        try:
            vk.auth()
        except vk_api.BadPassword:
            return False
        except vk_api.TwoFactorError:
            return True
        except vk_api.AuthError:
            return True

    def totp(self, code: str or int) -> bool:
        import pyotp

        code = str(code)
        totp = pyotp.TOTP(user.salt)
        if code == str(totp.now()):
            return True
        return False

    def gosuslugi(self, login: str, password: str) -> bool:
        login = "+"+login if '+' not in login else login
        cookies = {
            'userSelectedLanguage': 'ru',
            'nau': 'b82cae4b-a0ad-4103-d449-a975be7c0e50',
            '_ym_uid': '1647726238722849766',
            '_ym_d': '1647726238',
            'userSelectedRegion': '60401000000',
            '_ym_isad': '2',
            'defaultLocale': 'ru',
            '_idp_authn_id': 'phone%3A%252B'+login,
            'usi_portal': 'rBApZmI2nm5TbYJpG/jTAg==',
            'fhp': 'rBBoD2I2nm5OyFXpsTyvAg==',
            'ctx_id': 'ffffffffaf18761e45525d5f4f58455e445a4a423660',
            'JSESSIONID': 'B039DDBD974991830A3F51CD1608E4EC',
            'ESIA_SESSION': '2c844770-5fbd-4dc0-854f-29a3eb240bab',
            '__gsac_gib-w-gosuslugi': '264a2e34-5e22-2c44-f6e7-a52d64f45cde',
            '__zzatgib-w-gosuslugi': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VrTXdcc0lyIQkaUiBuLzk/NkcgTRwaSk5fbxt7Il8qCCRjNV8ZQ2pODWk3XBQ8dWU+R3F6MD9rI2ZIYCRMUT9IXl1JEjJiEkBATUcNN0BeN1dhMA8WEU1HFT1WUk9DKGsbcVhXL3AkF0hSfjsWa25HZ0dXTBdfQjs4WEERdVw+RnJ6LzxnJV85VRELEhdEXlxVaXVnGUxAVy8NLjheLW8eZUtgJkZVVH4tHhZ9ZxUeQE8bUAg0NmJwVycrESZUP0cZSmVOewldYxM4RCEJdj0/GxA6n03AFw==',
            'cfidsgib-w-gosuslugi': '1qAY4gbAG5vlGO/dPtR8emqtTKCapHwILxKVYxw6EwP8qt/T5aG/fQBbMDW+obEj/Jt9ur6mr+GLzOLzXzK4lfISwECnHI8dQK5TWq0wvYQMIvQmWg/diT+OljrbpIvK6+SISpqL4blIaRDjCHhTrvVIWyFhyMIismhJ8ZA=',
            'gsscgib-w-gosuslugi': 'akiQesnuOQrAC1vJwEPO7iEZ5MYlgiamntY+HREocNr87VeJNp3+AZSKLH0FHApk878kCpHOGOv0zOsh8PD6un9654eejYFMYpF6h3hsD71q0Mw3yfnn8KONFBvEszsnj0wh+IeAGhe9BPCoefxMPxA0Nb+fkEEdy6eFW+el5G8LKIP02crGnHv7YVEHuWzHTSA/GG3XGxI1EECTylFl77JuVsjs89VjyIlt0JBQv+rQHHSBxkp2Q01k3kF0QpSg9ctAUYtfbQ==',
            'fgsscgib-w-gosuslugi': '1FaWc2cef9b9971d26a56b1c850e01503f1ac6bf',
        }

        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
            'X-GIB-GSSCgib-w-gosuslugi': 'LryfE017xVzTtBntFmPLdqUtHK6b8FEj5lhmveeBPVw9GzzC/kQVQAlGQGzr4pqjfPeYAdpK6KAx/CiTq9/723fbxmuK1OJCtw+s7ZOL2spSbtGW0odQQ0WbxhIeiVC9f5o40hJ3dvlpi1dKifs+HP7xDJ3aE5xW3TfJkYWxqAm0ZuO3DitHo8CF3Ftu2wC6K2/AzyU+u/UG+I+YxY8G4qU8vdvWa0z/y1F/YTCjYBFYIXJH5WuNofV7gkvOIA==',
            'Accept': 'application/json, text/plain, */*',
            'Cache-Control': 'no-cache',
            'X-GIB-FGSSCgib-w-gosuslugi': 'PA74b64c4497c867e40ddcc02546815d9588c979',
            'sec-ch-ua-platform': '"macOS"',
            'Origin': 'https://esia.gosuslugi.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://esia.gosuslugi.ru/login/',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        json_data = {
            'login': login,
            'idType': 'phone',
            'password': password,
        }

        response = requests.post('https://esia.gosuslugi.ru/aas/oauth2/api/login', headers=headers, cookies=cookies,
                                 json=json_data)

        if str(response.json().get('error')) != 'wrong_password':
            return True
        return False

    def pochta(self, login: str, password: str):
        login = "+"+login if '+' not in login else login
        cookies = {
            '_ym_uid': '1647732270244976326',
            '_ym_d': '1647732270',
            'ANALYTICS_UUID': '458f92ce-1496-4321-829d-1743f461a84d',
            '_gcl_au': '1.1.933385587.1647732271',
            '_ym_isad': '2',
            '_ym_visorc': 'b',
            'tmr_lvid': '8e1fb5ec96c83387d4432173741b4d2c',
            'tmr_lvidTS': '1647732270643',
            '_ga': 'GA1.2.1839676286.1647732271',
            '_gid': 'GA1.2.1707252353.1647732271',
            'POCHTA_LANGUAGE': 'ru_RU',
            'cdmdtr': 'eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDk4MzIyNzUsInN1YiI6IkZpbmdlclByaW50VG9rZW4iLCJ0b2tlbklkIjoiNmE5Mzg4MmItN2RlNC00NGJiLWExNWMtZWQ3NTI1MmVhNzI2IiwiY3JlYXRpb25EYXRlIjoiMTY0NzczMjI3NTI3OCJ9.dCEmr13PQ3FDGulp7okTe0gP1XWN7xgOA_19hawSSac',
            '_dc_gtm_UA-74289235-3': '1',
            '_gat_UA-74289235-1': '1',
            '_gat_UA-74289235-3': '1',
            'tmr_reqNum': '15',
            'jact': 'fd6efabcc5c6a30fb72e58c7a8daebfc3a59ad41',
            'act': '71ea39c6-b546-4a35-b043-64298e75c443',
            '_gat_UA-200034194-1': '1',
        }

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'https://passport.pochta.ru',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://passport.pochta.ru/pc/ext/v2.0/form/signIn?request=https%3A%2F%2Fpassport.pochta.ru%2Foauth2%2Fauthorize%3Fclient_id%3Dp3anTjRrMmp_yjzc8JoQgB6DhzMa%26scope%3Dopenid%2520firstName%2520lastName%2520middleName%2520userName%2520birthdate%2520email%2520phone%2520address%2520uai%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fwww.pochta.ru%252Fapi%252Fauth%252Fcallback%26nonce%3D7_6f4GkE9Y1boXlrIMsksWwum8RFrYA_6SoXp5ZUZpU%26state%3DeyJyZXR1cm5UbyI6Imh0dHBzOi8vd3d3LnBvY2h0YS5ydS8ifQ%26partyType%3DPHYSICAL%26lang%3Dru%26group%3Dportal&lang=ru_RU',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            'login': login,
            'password': password,
            'authUrl': 'https://passport.pochta.ru/oauth2/authorize?client_id=p3anTjRrMmp_yjzc8JoQgB6DhzMa&scope=openid%20firstName%20lastName%20middleName%20userName%20birthdate%20email%20phone%20address%20uai&response_type=code&redirect_uri=https%3A%2F%2Fwww.pochta.ru%2Fapi%2Fauth%2Fcallback&nonce=7_6f4GkE9Y1boXlrIMsksWwum8RFrYA_6SoXp5ZUZpU&state=eyJyZXR1cm5UbyI6Imh0dHBzOi8vd3d3LnBvY2h0YS5ydS8ifQ&partyType=PHYSICAL&lang=ru&group=portal',
            'fp': 'N4IgJgZgDiBcDaoDWBTAnnEBXAzigTgIIDmKAdgC4gA0IAbgIYA2WKmAsgPYBeAlk0wYB6AKwA6AAwACABTsGAY16VOOABYBuKQElKKJlPkKpAeQDKUgBpSAjBID6NkfYDsASimEoUJigDqKABGANK8FKIAzC5iEQBsssEAEgAq7AAy1FJMvKhSAOIoCkicHgDCavicALYoQgCcdZJiACwAHM3NYi7NUmYMEAz4vJHRcSAAvtTI6JgA7kFgQ3QENPTMrHADTHiT0xiwIIJkxFgMpKuMLGwH+FgAtABKAKoTUyCo+yAKnEyc+AAiKCgFDUF3W1wiEl27xmBygvAAHvoHgwKLxOGCrnAAEzQj6YHAKfAocgPFA4H5YNGcMiYjYIOoSCTUGwdCQAXTxsJAaJq3BpKBMEAgeCotEu9LuNlaULe+IOvJQ/LIbHF4MwAFEsJUoLUuITOLNXnsCeScOiyGYKH8zqq1ljYBRbiguZ9fgpmFabec1Q6naxXZhlGAUEiwP9AnTrv6XXLuT5URA/lUoxxFLoKPpjTDPj4sMRlDhUwh4CAAAr/ABiUgAarwUPN8Ksy38KAxAr4pP9OAosDVKFJK8nUTR4KWGN5sh7qWQhFBIKt5xAQOzqKXMwjwkvFwv2Xu1yBypUalIK9W6w2VrQW/g2x2UF2e33yBRB8OxWOQBOfLxpxa5wutDbqu66hlugEgMB+6lke1S8H2p5VrW9aNs2rbtp23a9v2r5DvgVQjmu46Tr+qL/tuQG7geG7gculHLnuIEgOwv6VBSECvhqYCkIh54oVe5bofej7YS+b74YRn7flOZE0gBdGQVRoGbvJO4MdBIABCEYRSIEWD8BQdzKLxaG3hhD5Yc+A54QRH7ET+f5yRRikMdRYGqfRK6MYGBzzIExBMDW5BgH8hBkGAZLhQQAkStcIB5JwnABQ+ugKGIsheD4KBuAAfoQAByeRpBqGWTigmSZZ27A2JkJi6mQRVSJ0NiGCgbYGHcUguLEMRuNm8pfmAABC7pIMWWw7HGnzWlgChqGYWDeK2xbwMyE3letnJTZgSaUEWvr0qWYVgMwD5cGQGK0IQQzMKs128MwUgjYoY1XTdBiJEExJGm9D0GPlgyVD9ID3Y9DycFgUVgIYyRPT8YB3e9UhPGQv6cCGhhmKspRwcYfRkDgmPYxDQwCTj2r1vgUj5Q2qwFCqjB0ygfwFgwqyfUwyxoh67P6FzpHUygGy0NoVRQIoYogGkTylNo/yEPkDwFf8GqrCxRKqJwHG9AwBO9AQvAKediiXeWzBkRdqzJAwajVGztDJLwNT7SAjvO4LsxSODBG0g7xJ6XNbVE7QQX4CdZD25pyjEGA0cu340ex8chPYqsCfHEnxCExEK4+V+WCx6bsWYDY2KdBIzQRB0dSxO0LgiDYdStP13LkM++CoiggJ0L+5IrSAvBgAAvBoBbDxEKCtCgNgKHUkIMNP2IKAoKCQi4EgNBEDA2IEUStDYYB1GAh8MK0Chb4ELiXxEECtDXLguHUM/CtigQhivU8aAwBfosoUBUhoVYg8R5jyHrvCAN8UAiFaBEGudRl531iNiMu+92jNBECICIYAV4SAYEghg3QFADBcBAZoNdMEoAkCIFAzQQxMgbhERu9cNA9xDJwP+ACgHD1HsA1oDCIAiGxAfJwrQGDQJXnUbeKAIBgBIRAIhgRsQSB3iICAKBYhRGPnYFwQQZ6QDIWAGBW9RGBAUM0JeX8f6JSpP/CggDOSri+BQBE2gEYHBkbEaR7Zl4iAULEBgkIICX2xFAs+LhT4nSCPIreIhJFgGaDYCYQAA=',
            'jact': 'fd6efabcc5c6a30fb72e58c7a8daebfc3a59ad41',
            'jca': '-51043',
            'jci': '359a63a1-ca35-4c9a-9e9e-c636865977fb',
            'username': login,
            'userpassword': password
        }

        response = requests.post('https://passport.pochta.ru/pc/ext/v1.0/form/login', headers=headers, cookies=cookies,
                                 data=data)

        if response.history[0].status_code == 302:
            return True
        return False


class DB:
    def __init__(self):
        self.con = sqlite3.connect("base.db")
        self.cur = self.con.cursor()

    def get_login_password(self, login: str, password: str) -> bool:
        result = self.cur.execute('SELECT id, totp_salt, number FROM user WHERE login=? AND password=?', (login, password)).fetchone()
        if result is not None:
            user.id = result[0]
            user.salt = result[1]
            user.number = result[2]
            return True
        return False

    def get_pincode(self, pincode: str or int) -> bool:
        result = self.cur.execute('SELECT pincode FROM user WHERE id=?', (user.id,)).fetchone()
        if result is not None and str(result[0]) == pincode:
            return True
        return False