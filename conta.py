class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto.... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if(valor <= (self. __saldo + self. __limite)):
            self.saldo -= valor
        else:
            print("O valor {} passou o limite.". format(valor))

    def transfere(self, valor, origem, destino):
        origem.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001 - Banco do Brasil"