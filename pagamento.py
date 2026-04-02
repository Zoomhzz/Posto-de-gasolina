from combustivel import listar_produto, produtos
pagamentos = []

def pagamento():
    listar_produto()
    codigo = input("Digite o código do combustível desejado: ")
    if codigo not in produtos:
        print("Produto não encontrado!")
        return

    litros = float(input("Digite a quantidade de litros: "))
    produto = produtos[codigo]

    if litros > produto["quantidade"]:
        print("Quantidade indisponível em estoque!")
        return

    preco_total = litros * produto["preco"]
    print("Formas de pagamento:\n1 - Pix\n2 - Cartão de Débito\n3 - Dinheiro\n4 - Cartão de Crédito")
    forma_pagamento = input("Escolha a forma de pagamento: ")

    if forma_pagamento in ["1", "2", "3"]:
        desconto = preco_total * 0.10
        preco_total -= desconto
    else:
        desconto = 0

    produtos[codigo]["quantidade"] -= litros
    pagamentos.append({"codigo": codigo, "litros": litros, "total": preco_total, "forma": forma_pagamento})

    print(f"Pagamento realizado com sucesso! Total a pagar: R${preco_total:.2f} (Desconto: R${desconto:.2f})")