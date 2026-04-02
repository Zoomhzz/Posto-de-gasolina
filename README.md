um sistema de gerenciamento via linha de comando (CLI) desenvolvido em Python para otimizar as operações básicas de um posto de combustíveis. Este projeto foi estruturado de forma modular para facilitar a manutenção e escalabilidade, simulando um ambiente real de controle de estoque, clientes e vendas.

🚀 Funcionalidades
O sistema é dividido em quatro pilares principais:

Gestão de Produtos: Cadastro, listagem, pesquisa e alteração de combustíveis, com controle rigoroso de preço e litragem em estoque.

Gestão de Clientes & Fornecedores: Módulos completos para cadastro e consulta de dados essenciais (CPF/CNPJ, contatos e nomes).

Módulo de Vendas e Pagamentos:

Processamento de vendas com baixa automática no estoque.

Cálculo dinâmico de preços.

Lógica de Desconto: Aplicação de 10% de desconto para pagamentos via Pix, Dinheiro ou Débito.

Interface Intuitiva: Menu interativo via terminal com navegação simples e direta.

🛠️ Tecnologias Utilizadas
Python 3.10+: Utilização de match-case para um fluxo de controle mais limpo e legível.

Modularização: Divisão do código em diferentes arquivos (main.py, combustivel.py, pagamento.py) seguindo boas práticas de organização.

Dicionários: Uso de estruturas de dados eficientes para persistência em memória durante a execução.
