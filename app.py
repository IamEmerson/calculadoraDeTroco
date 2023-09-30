class CalculadoraDeTroco():

    def __init__(self, valor_total, valor_pago):
        self.valor_total = valor_total
        self.valor_pago = valor_pago

    def calcular_troco(self):
        if self.valor_pago < self.valor_total:
            return "Valor pago insuficiente"
        
        troco = self.valor_pago - self.valor_total
        return troco


valor_total_compra = 50.0
valor_pago_cliente = 70.0

calculadora = CalculadoraDeTroco(valor_total_compra, valor_pago_cliente)

troco_calculadora = calculadora.calcular_troco()

print("O troco a ser devolvido é: R$", troco_calculadora)
