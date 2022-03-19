import mysql.connector
import logging

logging.basicConfig(level=logging.INFO)


class Db:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='qwerty1234',

            port=3306
        )
        logging.info('OKEY')
        self.cursor = self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


if __name__ == '__main__':
    Db()
