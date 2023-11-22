

class User:

    def __init__(self, name, accountNumber, balance, creditLimit):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance
        self.creditLimit = creditLimit
        self.debt = 100

    def imprimirSaldo(self, args):
        return "Seu saldo é de R$ " + str(self.balance)

    def imprimirLimite(self, args):
        return "Seu limite é de R$ " + str(self.creditLimit)

    def processarPagarFatura(self, args):
        try:
            amount = float(args[0])
        except:
            return "Não entendi o valor que você quer pagar"
        return self.pagarFatura(amount)
    
    def processarFaturaTotal(self, args):
        if self.debt > self.balance:
            return "Sua dívida é maior que seu saldo, não foi possível realizar operação"
        return self.pagarFatura(self.debt)


    def pagarFatura(self, amount):
        if amount > self.balance:
            return "Saldo insuficiente"
        else:
            self.balance -= amount
            self.debt -= amount
            return "Fatura paga com sucesso"

    def processarTransferir(self, args):
        try:
            amount = float(args[0])
        except:
            return "Não entendi o valor que você quer transferir"
        return self.transferir(amount)

    def transferir(self, amount):
        if amount > self.balance:
            return "Saldo insuficiente"
        else:
            self.balance -= amount
            return "Transferência realizada com sucesso"
    
    def processarEmprestimo(self, args):
        try:
            amount = float(args[0])
        except:
            return "Deve Informar o valor do empréstimo"
        if amount > self.creditLimit - self.debt:
            return "Seu perfil não permite um empréstimo desse valor. Tente um valor menor."
        else:
            self.debt += amount
            self.balance += amount
            return "Crédito obtido com sucesso"
    
    def mostrarJurosEmprestimo(self, args):
        return "A taxa de juros atual sobre seus empréstimos é de 12% ao mês."


    def imprimirDivida(self, args):
        return "Sua dívida é de R$ " + str(self.debt)

    def mostrarMenu(self, args):
        return """Por favor, escolha uma das opções abaixo:
        - Mostrar saldo
        - Consultar limite no crédito disponível
        - Pagar fatura do cartão de crédito
        - Pagar uma parte da fatura do cartão de crédito
        - Fazer transferência para outro banco (informar o valor)
        - Pegar empréstimo (informar o valor)
        """