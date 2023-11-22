

class TagMap:

    def __init__(self, user):
        self.user = user
        self.tags = {
            "<imprimir saldo>": user.imprimirSaldo,
            "<consultar limite livre>": user.imprimirLimite,
            "<pagar fatura>": user.processarPagarFatura,
            "<pagar fatura total>": user.processarFaturaTotal,
            "<consultar debt>": user.imprimirDivida,
            "<transferir>": user.processarTransferir,
            "<pegar emprestado>": user.processarEmprestimo,
            "<consultar juros emprestimo>": user.mostrarJurosEmprestimo,
            "<menu>": user.mostrarMenu,
            "<erro>": user.mostrarMenu
        }