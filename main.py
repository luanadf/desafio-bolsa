# Importações
import util
from Caixa import Caixa

# Prints iniciais
print(util.FRASE_SEPARADOR)
print(util.FRASE_INICIAL)
print(util.FRASE_SEPARADOR)

# Criação de um "Caixa"
caixa = Caixa()

# Função que realiza a operação de depósito
def operacaoDeposito():
    print(util.FRASE_DEPOSITO)
    while True:
        cedulas = {
            100: 0,
            50: 0,
            20: 0,
            10: 0
        }

        print(util.FRASE_DIGITE_QNT_CEDULAS)
        
        # Testa se os valores inseridos são válidos
        try: 
            cedulas[10] = int(input("R$ 10,00: "))
            cedulas[20] = int(input("R$ 20,00: "))
            cedulas[50] = int(input("R$ 50,00: "))
            cedulas[100] = int(input("R$ 100,00: "))
        except:
            print(util.FRASE_VALOR_INVALIDO)
            break

        # Valor total do depósito
        total = cedulas[10]*10 + cedulas[20]*20 + cedulas[50]*50 + cedulas[100]*100

        # Imprime na tela as quantidade de cédulas a serem depositadas e o valor total
        print(util.FRASE_CONFIRMACAO_DEPOSITO 
            % (cedulas[10], cedulas[20], cedulas[50], cedulas[100], total))

        # Solicita ao usuário uma confirmação dos valores
        print(util.FRASE_CONFIRMA_SUA_ESCOLHA)
        confirmaEscolhaInput = input(util.FRASE_DIGITE).upper()

        # Se o usuário confirma, chama a função de deposito do módulo "Caixa"
        # passando como parâmetro a quantidade de cada cédula
        if confirmaEscolhaInput.isalpha() and confirmaEscolhaInput in util.V_OPCOES_CONFIRMACAO:
            if confirmaEscolhaInput in util.V_SIM:
                caixa.deposito(cedulas)
                print(util.FRASE_DEPOSITO_REALIZADO)
                break
            else:
                break
        else:
            print(util.FRASE_VALOR_INVALIDO)    

# Função que realiza a operação de saque
def operacaoSaque():
    print(util.FRASE_)
    while True:
        print(util.FRASE_DIGITE_VALOR_SAQUE)
        # Testa se os valores inseridos são válidos
        try: 
            valor = int(input(util.FRASE_DIGITE))
        except:
            print(util.FRASE_VALOR_INVALIDO)
            break
        
        # Chama a função de saque do módulo "Caixa" passando como parâmetro 
        # o valor solicitado
        cedulasSaque = caixa.saque(valor)

        # Se a função retorna um dicionário com a quantidade de cédulas, o saque foi aprovado
        # se ela retorna 0, o saque foi negado
        if cedulasSaque == 0:
            print(util.FRASE_SAQUE_NEGADO)
            break
        else:
            # Printa uma mensagem de saque aprovado e quais foram as cédulas liberadas
            print(util.FRASE_SAQUE_APROVADO)
            print(util.FRASE_CEDULAS_LIBERADAS 
                % (cedulasSaque[10], cedulasSaque[20], cedulasSaque[50], cedulasSaque[100], valor))
            break

# Loop que chama as determinadas funções das operações escolhidas
# 1 = operação de depósito
# 2 = operação de saque
# q = sair
while True:
    print(util.FRASE_SELECIONAR_OPERACAO)
    operacao = input(util.FRASE_DIGITE)

    if operacao == "1":
        operacaoDeposito()
        print(util.FRASE_SEPARADOR)

    elif operacao == "2":
        operacaoSaque()
        print(util.FRASE_SEPARADOR)

    elif operacao == "q":
        quit()
    else:
        print(util.FRASE_VALOR_INVALIDO)

