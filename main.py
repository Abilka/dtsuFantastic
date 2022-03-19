import typing

import auth
import auth_method

if __name__ == '__main__':
    print(auth_method.auth_method)
    for service in auth_method.auth_method:
        root = auth.MainApp()
        result = root.generate_auth(service.inputs, service.name)
        del root
        print(result)