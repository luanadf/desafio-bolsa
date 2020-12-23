import unittest
from Caixa import Caixa

# Testes unitários que fazem a verificação dos requisitos solicitados no problema
class VerificarSistemaTests(unittest.TestCase):
    # Registrar o abastecimento de notas de 10, 20, 50 e 100 no caixa eletrônico
    def test_registra_deposito(self):
        # Organizar variáveis
        caixa = Caixa()
        cedulas = {
            100: 1,
            50: 2,
            20: 3,
            10: 4
        }
      
        # Agir
        caixa.deposito(cedulas)
        
        # Conferir resultados
        self.assertEqual(cedulas, caixa.getCedulasDisponiveis())

    # Aprovar ou rejeitar o saque de uma determinada quantia
    # Informar quais notas devem ser liberadas para um saque aprovado
    def test_aprova_ou_rejeita_saque(self):
        # Organizar variáveis
        caixa = Caixa()
        
        cedulas = {
            100: 1,
            50: 2,
            20: 3,
            10: 4
        }
        caixa.deposito(cedulas)

        cedulasSaqueAprovado = {
            100: 0,
            50: 0,
            20: 0,
            10: 1
        }

        # Agir
        saqueAprovado = caixa.saque(10)
        saqueRejeitado = caixa.saque(5)
        
        # Conferir resultados
        self.assertEqual(saqueAprovado, cedulasSaqueAprovado)
        self.assertEqual(saqueRejeitado, 0)

    # O saque deve ser rejeitado caso a quantia solicitada for maior que a 
    # quantia existente em caixa
    def test_rejeita_saque_com_quantia_maior_que_saldo(self):
        # Organizar variáveis
        caixa = Caixa()
        cedulas = {
            100: 1,
            50: 2,
            20: 3,
            10: 4
        }
      
        # Agir
        saqueRejeitado = caixa.saque(1000)
        
        # Conferir resultados
        self.assertEqual(saqueRejeitado, 0)
    
    # O saque deve ser rejeitado caso não existam notas que permitam completar 
    # a quantia solicitada
    def test_rejeita_saque_com_notas_insuficientes_no_caixa(self):
        # Organizar variáveis
        caixa = Caixa()
        cedulas = {
            100: 0,
            50: 0,
            20: 2,
            10: 0
        }
      
        # Agir
        saqueRejeitado = caixa.saque(30)
        
        # Conferir resultados
        self.assertEqual(saqueRejeitado, 0)