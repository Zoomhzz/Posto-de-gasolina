produtos = {}

def aba_produtos():
    op = input("Bem-vindo à aba de produtos!\n1 - Cadastrar produto\n2 - Ver lista\n3 - Pesquisar\n4 - Alterar\nOpção: ")
    match op:
        case "1": cadastro_produto()
        case "2": listar_produto()
        case "3": pesquisar_produto()
        case "4": alterar_produto()

def cadastro_produto():
    codigo = input("Código do produto: ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = float(input("Quantidade em litros: "))
    produtos[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade}
    print("Produto cadastrado com sucesso!")

def listar_produto():
    if not produtos:
        print("Nenhum produto cadastrado")
        return
    for codigo, dados in produtos.items():
        print(f"Código: {codigo} | Nome: {dados['nome']} | Preço: R${dados['preco']:.2f} | Quantidade: {dados['quantidade']}L")

def pesquisar_produto():
    codigo = input("Informe o código do produto: ")
    if codigo in produtos:
        dados = produtos[codigo]
        print(f"Código: {codigo} | Nome: {dados['nome']} | Preço: R${dados['preco']:.2f} | Quantidade: {dados['quantidade']}L")
    else:
        print("Produto não encontrado")

def alterar_produto():
    codigo = input("Informe o código do produto: ")
    if codigo in produtos:
        nome = input("Novo nome: ")
        preco = float(input("Novo preço: "))
        quantidade = float(input("Nova quantidade: "))
        produtos[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade}
        print("Produto alterado com sucesso!")
    else:
        print("Produto não encontrado")