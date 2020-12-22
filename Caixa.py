# Classe Caixa
class Caixa:
    # Construtor: o caixa inicia sem cédulas e com saldo = 0
    def __init__(self):
        self.__cedulasDisponiveis = {
            100: 0,
            50: 0,
            20: 0,
            10: 0
        }
        self.__saldo = 0

    # Função de depósito, recebe como parâmetro um dicionário indicando a 
    # quantidade de cada cédula que foi depositada
    def deposito(self, cedulas):
        self.__cedulasDisponiveis[100] += cedulas[100]
        self.__cedulasDisponiveis[50] += cedulas[50]
        self.__cedulasDisponiveis[20] += cedulas[20]
        self.__cedulasDisponiveis[10] += cedulas[10]

        # Realiza a soma das cédulas recebidas e adiciona ao saldo do caixa
        totalDeposito = cedulas[10]*10 + cedulas[20]*20 + cedulas[50]*50 + cedulas[100]*100
        self.aumentarSaldo(totalDeposito)

    # Função de saque, recebe como parâmetro o valor solicitado
    def saque(self, valor):
        valorInicial = valor
        
        # Se o valor solicitado for maior do que o saldo do caixa, retorna 0
        # Saque negado
        if valor > self.getSaldo():
            return 0
        
        cedulasSaque = {
            100: 0,
            50: 0,
            20: 0,
            10: 0
        }

        cedulasCaixa = self.__cedulasDisponiveis

        # Loop que separa o mínimo de cédulas necessárias para chegar ao valor
        for i in cedulasCaixa:
            qntCedulas = int(valor / i)
            if cedulasCaixa[i] != 0:
                if (qntCedulas - cedulasCaixa[i]) >= 0:
                    cedulasSaque[i] += cedulasCaixa[i]
                    valor -= cedulasCaixa[i]*i
                else:
                    cedulasSaque[i] += qntCedulas
                    valor -= qntCedulas*i

        # Se a soma das cédulas calculada acima nao "zerar" o valor solicitado,
        # significa que não há cedulas que completem a quantia
        # Saque negado
        if valor != 0:
            return 0
        
        # Se houver a quantidade certa de cédulas as retiramos do caixa
        for i in cedulasCaixa:
            cedulasCaixa[i] -= cedulasSaque[i]

        # Diminuímos o valor do saldo
        self.diminuirSaldo(valorInicial)

        # E retornamos um dicionário contendo a quantidade de cada cédula a liberar
        return cedulasSaque

    # Getter das cédulas disponíveis
    def getCedulasDisponiveis(self):
        return self.__cedulasDisponiveis

    # Getter do saldo
    def getSaldo(self):
        return self.__saldo

    # Função que aumenta o saldo
    def aumentarSaldo(self, valor):
        self.__saldo += valor

    # Função que diminui o saldo
    def diminuirSaldo(self, valor):
        self.__saldo -= valor