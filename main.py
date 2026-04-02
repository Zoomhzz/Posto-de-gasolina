from combustivel import aba_produtos, listar_produto
from pagamento import pagamento

clientes = {}
fornecedor = {}

def aba_clientes():
    op = input("Bem vindo à aba de clientes!\n1 - Novo cadastro\n2 - Ver lista\n3 - Pesquisar\n4 - Alterar cadastro\nOpção: ")
    match op:
        case "1": cadastro_cliente()
        case "2": listar_cliente()
        case "3": pesquisa_cliente()
        case "4": alterar_cliente()

def cadastro_cliente():
    nome = input("Informe seu Nome: ")
    cpf = input("Informe seu CPF: ")
    telefone = input("Informe seu Telefone: ")
    email = input("Informe seu Email: ")
    clientes[cpf] = {"nome": nome, "telefone": telefone, "email": email}
    print("Cadastro realizado com sucesso!")

def listar_cliente():
    if not clientes:
        print("Nenhum cliente cadastrado.\n")
        return
    for cpf, dados in clientes.items():
        print(f"CPF: {cpf} | Nome: {dados['nome']} | Telefone: {dados['telefone']} | Email: {dados['email']}")

def pesquisa_cliente():
    cpf = input("Informe o CPF: ")
    if cpf in clientes:
        print(f"Nome: {clientes[cpf]['nome']}\nTelefone: {clientes[cpf]['telefone']}\nEmail: {clientes[cpf]['email']}")
    else:
        print("Cliente não encontrado")

def alterar_cliente():
    cpf = input("Informe o CPF: ")
    if cpf in clientes:
        nome = input("Novo nome: ")
        telefone = input("Novo telefone: ")
        email = input("Novo email: ")
        clientes[cpf] = {"nome": nome, "telefone": telefone, "email": email}
        print("Cadastro atualizado com sucesso!")
    else:
        print("Cliente não encontrado")

def aba_fornecedor():
    op = input("Bem-vindo à aba de fornecedores!\n1 - Cadastrar\n2 - Pesquisar\n3 - Alterar\nOpção: ")
    match op:
        case "1": cadastro_fornecedor()
        case "2": pesquisar_fornecedor()
        case "3": alterar_fornecedor()

def cadastro_fornecedor():
    cnpj = input("CNPJ: ")
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    fornecedor[cnpj] = {"nome": nome, "email": email, "telefone": telefone}
    print("Fornecedor cadastrado com sucesso!")

def pesquisar_fornecedor():
    cnpj = input("Informe o CNPJ: ")
    if cnpj in fornecedor:
        print(f"Nome: {fornecedor[cnpj]['nome']}\nTelefone: {fornecedor[cnpj]['telefone']}\nEmail: {fornecedor[cnpj]['email']}")
    else:
        print("Fornecedor não encontrado")

def alterar_fornecedor():
    cnpj = input("Informe o CNPJ: ")
    if cnpj in fornecedor:
        nome = input("Novo nome: ")
        telefone = input("Novo telefone: ")
        email = input("Novo email: ")
        fornecedor[cnpj] = {"nome": nome, "email": email, "telefone": telefone}
        print("Cadastro atualizado com sucesso!")
    else:
        print("Fornecedor não encontrado")

def tabela_preco():
    listar_produto()

def menu():
    while True:
        print("\nBem-vindo ao Posto As!\n1 - Fornecedores\n2 - Clientes\n3 - Produtos\n4 - Tabela de Preços\n5 - Pagamento\n6 - Sair")
        op = input("Escolha uma opção: ")
        match op:
            case "1": aba_fornecedor()
            case "2": aba_clientes()
            case "3": aba_produtos()
            case "4": tabela_preco()
            case "5": pagamento()
            case "6": print("Volte sempre!"); break
            case _: print("Opção inválida!")

menu()