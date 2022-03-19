import auth
import auth_method
import error_window


def check_service(service: auth_method.AuthMethod):
    root = auth.MainApp()
    result = root.generate_auth(service.inputs, service.name)
    del root
    print(result)
    return service.func_check(*result)

if __name__ == '__main__':
    for service in auth_method.auth_method:
        while check_service(service) is not True:
            error_window.MainApp()


