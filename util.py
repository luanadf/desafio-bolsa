'''
Arquivo utilitário com strings e valores para o programa
'''

'''
* LEGENDA DOS RADICAIS *
    FRASE_: String que será printada na interface do programa
    V_: Vetor
'''

FRASE_INICIAL =  "                       --- CAIXA ---"\

FRASE_DEPOSITO =  "\n--- DEPOSITO ---"\

FRASE_SAQUE =  "\n--- SAQUE ---"\

FRASE_VALOR_INVALIDO = "\nPor favor, insira um valor válido!\n"

FRASE_SELECIONAR_OPERACAO = "\nSelecione a operação:"\
    "\n"\
    "\nDigite 1 para Depósito"\
    "\n       2 para Saque"\
    "\n       q para Sair"

FRASE_DIGITE = "\nDigite: "

FRASE_DIGITE_QNT_CEDULAS = "\nDigite quantas cédulas de cada você quer depositar:"

FRASE_CONFIRMACAO_DEPOSITO = "\nVocê deseja depositar:"\
                                "\n - %d cédula(s) de R$ 10,00"\
                                "\n - %d cédula(s) de R$ 20,00"\
                                "\n - %d cédula(s) de R$ 50,00"\
                                "\n - %d cédula(s) de R$ 100,00"\
                                "\nTotal: R$ %d,00"

FRASE_CONFIRMA_SUA_ESCOLHA = "\nConfirma os valores? (S/N)"

FRASE_DEPOSITO_REALIZADO = "\nDepósito realizado com sucesso!\n"

FRASE_DIGITE_VALOR_SAQUE = "\nQual valor que voce deseja sacar? "

FRASE_SAQUE_NEGADO = "\nSaque negado! Tente novamente com outro valor."

FRASE_SAQUE_APROVADO = "\nSaque aprovado!"

FRASE_CEDULAS_LIBERADAS = "\nCédulas liberadas:"\
                                "\n - %d cédula(s) de R$ 10,00"\
                                "\n - %d cédula(s) de R$ 20,00"\
                                "\n - %d cédula(s) de R$ 50,00"\
                                "\n - %d cédula(s) de R$ 100,00"\
                                "\nTotal: R$ %d,00\n"

FRASE_SEPARADOR = "="*60

V_SIM = ['S', 'Y']

V_NAO = ['N']

V_OPCOES_CONFIRMACAO = []
V_OPCOES_CONFIRMACAO.extend(V_SIM)
V_OPCOES_CONFIRMACAO.extend(V_NAO)