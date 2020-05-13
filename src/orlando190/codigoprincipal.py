class PC:
    def __init__(self, procesador, ram):
        self.procesador = procesador
        self.ram = ram
    def imprimirInfo(self):
        print(f"PC \n procesador: {self.procesador} \n ram: {self.ram}")

