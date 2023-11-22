

menuInstruction = """
Você deve traduzir o comando textual para um dos seguintes comandos:
(em caso de dúvidas, escolha uma única opção). A opção deve seguir o seguinte formato:
<opcao> <argumento1> <argumento2> ... <argumentoN>
Não retorne mais nada além da opção e dos argumentos.
Você deverá incluir os sinais de menor e maior (< e >) na sua resposta.
"""

menuOptions = """
<imprimir saldo>: mostra o saldo do usuário
<consultar limite livre>: mostra o total de crédito disponível para o usuário
<consultar debt>: mostra o total de crédito utilizado pelo usuário
<pegar emprestado> <valor>: pega dinheiro emprestado do banco
<transferir> <valor>: transfere um valor para uma conta
<pagar fatura> <valor>: paga uma parcela da conta do cartão de crédito
<pagar fatura total>: paga a fatura completamente
<consultar juros emprestimo>: mostra a taxa de juros dos empréstimos
<menu>: mostra as opções disponíveis
<erro>: nenhuma opção do menu foi reconhecida
"""

#<imprimir extrato>: mostra o histórico de transações do usuário

menuExample = """
examplo 1: '<imprimir saldo>'
exemplo 2: '<consultar limite livre>'
exemplo 3: '<transferir> <500> <123456>'
exemplo 4: '<pagar fatura> <124.25>'
"""

menu = menuInstruction + menuOptions + menuExample

fixMenu = "Você deve corrigir o formato da mensagem, seguindo o seguinte formato:" + menuExample + \
"As opções disponíveis são:" + menuOptions + "Retorne apenas a opção e os argumentos, sem mais nada, no formato indicado acima, com < e >\n"

