import pymysql
import time, sys

class main:
    def __init__(self, t):
        self.t = t
        self.initial_t = t
    def connection_starter(self):
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='root',
                                    db='test_db',
                                    connect_timeout=30,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.t = self.initial_t

    def timer(self):
        while self.t > 0:
            print('Time left to reconnect: ', self.t, end='\r', flush=True)
            time.sleep(1)
            try:
                self.connection_starter()
            except Exception as e:
                self.t = self.t - 1             
        print("You run out of time")
        return sys.exit()

if __name__=='__main__':
    while True:
        a = main(15)
        try:
            print("Iniciando Conexion", end='\r', flush=True)
            a.connection_starter()
        except Exception as e:
            print("Error al intentar conectar, reintentando.")
            a.timer()