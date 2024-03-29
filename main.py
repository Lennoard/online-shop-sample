import json

from app import App
from auth.auth import UserAuth
from utils.utils import *
import getpass


def main():
    # inicializar (recuperar banco de dados)
    produtos = inicializar('produtos.bd')
    usuarios = inicializar('usuarios.bd')
    carrinho = []

    menu = tela_princiapal()
    opcao = int(input(menu))
    clear()

    while opcao != 0:
        if opcao == 1:
            iniciar_admin(produtos, usuarios)

        elif opcao == 2:
            iniciar_cliente(produtos, usuarios, carrinho)

        elif opcao == 3:
            iniciar_cadastro_usuario(usuarios)

        else:
            print('Opção inválida!\n')

        input('\n<enter> to continue...')
        opcao = int(input(menu))
        clear()

    finalizar('produtos.bd', produtos)
    finalizar('usuarios.bd', usuarios)


def tela_princiapal():
    menu = f'{Colors.INFO}***** Online Shop Sample *****{Colors.ENDC}\n'
    menu += '1 - Entrar como Admin\n'
    menu += '2 - Entrar como Cliente\n'
    menu += '3 - Cadastrar-se\n'
    menu += '0 - Finalizar programa\n'

    return menu


def iniciar_admin(produtos, usuarios):
    usuario = autenticar(usuarios)
    if usuario is None:
        clear()
        print_error('Credenciais incorretas')
        return

    if not usuario['admin']:
        clear()
        print_error('ACESSO NEGADO')
        return

    menu_admin = tela_principal_admin()
    opcao = int(input(menu_admin))
    clear()

    while opcao != 0:
        clear()
        if opcao == 1:
            # criar produto
            produto = novo_produto()
            produtos.append(produto)
            salvar('produtos.bd', produtos)

        elif opcao == 2:
            mostrar_produtos(produtos)

        elif opcao == 3:
            pesquisar_produto(produtos)

        else:
            print('Opção inválida!\n')

        input('\n<enter> to continue...')
        opcao = int(input(menu_admin))


def iniciar_cadastro_usuario(usuarios):
    print_info('Cadastrando novo usuario:\n')

    nome = input('Nome: ')
    email = input('Email: ')
    senha = getpass.getpass('Senha: ')

    usuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'admin': False
    }

    usuarios.append(usuario)


def tela_cliente(produtos, carrinho):
    clear()
    menu_cliente = tela_principal_cliente()
    opcao = int(input(menu_cliente))

    while opcao != 0:
        clear()
        if opcao == 1:
            pesquisar_produto_cliente(produtos, carrinho)

        elif opcao == 2:
            mostrar_produtos(produtos)

        elif opcao == 3:
            mostrar_carrinho(carrinho, produtos)  # verificar depois

        else:
            print('Opção inválida!\n')

        input('\n<enter> to continue...')
        opcao = int(input(menu_cliente))


def iniciar_cliente(produtos, usuarios, carrinho):
    usuario = autenticar(usuarios)

    if usuario is None:
        clear()
        print_error('Credenciais incorretas')
        return

    tela_cliente(produtos, carrinho)


def tela_principal_admin():
    menu_admin = f'\n{Colors.INFO}***** Online Shop Sample *****{Colors.ENDC}\n'
    menu_admin += '1 - Cadastrar novo produto\n'
    menu_admin += '2 - Listar produtos\n'
    menu_admin += '3 - Pesquisar produto\n'
    menu_admin += '0 - Sair\n'
    menu_admin += '\nOpção >>> '

    return menu_admin


def menu_cadastro_usuario():
    menu_admin = f'\n{Colors.INFO}***** Online Shop Sample *****{Colors.ENDC}\n'
    menu_admin += '1 - Cadastrar novo produto\n'
    menu_admin += '2 - Listar produtos\n'
    menu_admin += '3 - Pesquisar produto\n'
    menu_admin += '0 - Sair\n'
    menu_admin += '\nOpção >>> '

    return menu_admin


def tela_principal_cliente():
    menu_cliente = f'\n{Colors.INFO}***** Online Shop Sample *****{Colors.ENDC}\n'
    menu_cliente += '1 - Pesquisar produto\n'
    menu_cliente += '2 - Ver todos os produtos\n'
    menu_cliente += '3 - Carrinho de compras\n'
    menu_cliente += '0 - Sair\n'
    menu_cliente += '\nOpção >>> '

    return menu_cliente


def tela_carrinho():
    menu_carrinho = f'\n{Colors.INFO}***** Online Shop Sample *****{Colors.ENDC}\n'
    menu_carrinho += '1 - Ver Carrinho\n'
    menu_carrinho += '2 - Remover itens do Carrinho\n'
    menu_carrinho += '3 - Finalizar compra\n'
    menu_carrinho += '0 - Sair\n'
    menu_carrinho += '\nOpção >>> '

    return menu_carrinho


def sub_menu_admin():
    clear()
    submenu_admin = f'{Colors.INFO}Selecione a opção desejada:{Colors.ENDC}\n'
    submenu_admin += '1 - Mostrar detalhes\n'
    submenu_admin += '2 - Remover registro\n'
    submenu_admin += '3 - Editar produto\n'
    submenu_admin += '4 - Adicionar itens ao estoque\n'
    submenu_admin += '5 - Dar baixa em estoque\n'
    submenu_admin += '0 - Concluir pesquisa\n'
    submenu_admin += '\nOpção >>> '

    return submenu_admin


def sub_menu_cliente():
    clear()
    submenu_cliente = f'{Colors.INFO}Selecione a opção desejada:{Colors.ENDC}\n'
    submenu_cliente += '1 - Mostrar detalhes\n'
    submenu_cliente += '0 - Concluir pesquisa\n'
    submenu_cliente += '\nOpção >>> '

    return submenu_cliente


def novo_produto():
    clear()
    print_info('Adicionando novo produto:\n')

    nome = input('Nome: ')
    categoria = input('Categoria: ')
    marca = input('Marca: ')
    valor = float(input('Valor (R$): '))
    qtd_estoque = int(input('Quantidade cadastrada: '))

    produto = {
        'nome': nome,
        'categoria': categoria,
        'marca': marca,
        'valor': valor,
        'qtd_estoque': qtd_estoque
    }

    return produto


def mostrar_produtos(produtos):
    clear()
    qtd = len(produtos)
    if qtd == 0:
        print_warning('Nenhum produto encontrado')
        return

    print_info(f'Listando {qtd} produtos\n')

    for produto in produtos:
        print_nome_marca(produto)


def print_detalhes(produto):
    print('Nome: ', produto['nome'])
    print('Categoria: ', produto['categoria'])
    print('Marca: ', produto['marca'])
    valor = produto['valor']
    print(f'Valor: R$ {valor:.2f}')
    print('Quantidade em estoque: ', produto['qtd_estoque'])
    print(12 * '---')


def print_nome_marca(produto):
    print('Nome: ', produto['nome'])
    print('Marca: ', produto['marca'])
    print_info(12 * '---')


def pesquisar_produto(produtos):
    clear()
    menu = 'Digite a opção referente ao tipo de pesquisa\n'
    menu += '1 - Nome\n'
    menu += '2 - Categoria\n'
    menu += '3 - Marca\n> '

    opcao = int(input(menu))
    busca = []

    if opcao == 1:
        busca = pesquisa_nome(produtos)

    elif opcao == 2:
        busca = pesquisa_categoria(produtos)

    elif opcao == 3:
        busca = pesquisa_marca(produtos)

    else:
        print('Opção inválida!')
        pesquisar_produto(produtos)

    if len(busca) > 0:
        menu = sub_menu_admin()
        opcao = int(input(menu))

        if opcao == 1:
            detalhar_produto(busca, produtos)

        elif opcao == 2:
            remover_produto(busca, produtos)

        elif opcao == 3:
            editar_produto(busca, produtos)

        elif opcao == 4:
            add_estoque(busca, produtos)

        elif opcao == 5:
            baixa_estoque(busca, produtos)

        elif opcao == 0:
            main()

        else:
            print('Opção inválida!')
            opcao = int(input(menu))


def pesquisar_produto_cliente(produtos, carrinho):
    clear()
    menu = 'Digite a opção referente ao tipo de pesquisa\n'
    menu += '1 - Nome\n'
    menu += '2 - Categoria\n'
    menu += '3 - Marca\n> '

    opcao = int(input(menu))
    busca = []

    if opcao == 1:
        busca = pesquisa_nome(produtos)

    elif opcao == 2:
        busca = pesquisa_categoria(produtos)

    elif opcao == 3:
        busca = pesquisa_marca(produtos)

    else:
        print('Opção inválida!')
        pesquisar_produto(produtos)

    if len(busca) > 0:
        menu = sub_menu_cliente()
        opcao = int(input(menu))

        if opcao == 1:
            id = detalhar_produto(busca, produtos)
            add = input('Adicionar ao carrinho?\nS - SIM\nN - NÃO\n> ')
            add = add.upper()
            if add == 'S':
                carrinho.append(produtos[id])

        elif opcao == 0:
            tela_cliente(produtos, carrinho)

        else:
            print_error('Opção inválida!')
            opcao = int(input(menu))

    else:
        clear()
        print_warning('Nenhum resultado encontrado!')
        opcao = input('Pressione:\n1 - Nova pesquisa\n2 - Voltar ao menu inicial\n> ')  # aqui
        if opcao == 1:
            pesquisar_produto_cliente(produtos, carrinho)

        elif opcao == 2:
            tela_cliente(produtos, carrinho)


def detalhar_produto(busca, produtos):
    clear()
    for num in busca:
        print(f'ID produto: {num}')
        print_nome_marca(produtos[num])

    id_produto = int(input('Digite o ID do produto a detalhar: '))
    if id_produto in busca:
        print_detalhes(produtos[id_produto])
        return id_produto
    else:
        print('ID fora do intervalo da busca!\n')
        detalhar_produto(busca, produtos)


def detalhar_produto_cliente(busca, produtos):
    clear()
    for num in busca:
        print(f'ID produto: {num}')
        print_nome_marca(produtos[num])

    id_produto = int(input('Digite o ID do produto a detalhar: '))
    if id_produto in busca:
        print_detalhes(produtos[id_produto])
        return id_produto
    else:
        print('ID fora do intervalo da busca!\n')
        detalhar_produto_cliente(busca, produtos)


def remover_produto(busca, produtos):
    clear()
    for num in busca:
        print(f'ID produto: {num}')
        print('produto:', produtos[num]['nome'])
        print('---' * 12)

    id_produto = int(input('Digite o ID do produto a ser removido:\n> '))

    if id_produto in busca:
        print('produto', produtos[id_produto]['nome'], 'removido com sucesso!')
        del (produtos[id_produto])
    else:
        print('ID fora do intervalo da busca!\n')
        remover_produto(busca, produtos)


def editar_produto(busca, produtos):
    clear()
    for num in busca:
        print(f'ID produto: {num}')
        print('produto:', produtos[num]['nome'])
        print('---' * 12)

    id_produto = int(input('Digite o ID do produto a ser editado:\n> '))

    produto = novo_produto()
    produtos[id_produto] = produto


def add_estoque(busca, produtos):
    clear()
    for num in busca:
        print(f'ID produto: {num}')
        print('produto:', produtos[num]['nome'])
        print('Quantidade em estoque: ', produtos[num]['qtd_estoque'])
        print('---' * 12)

    id_produto = int(input('Digite o ID do produto a ser editado:\n> '))
    qtd = int(input('Digite a quantidade que será adicionada ao estoque:\n> '))

    produtos[id_produto]['qtd_estoque'] += qtd
    print('Adicionado com sucesso!')


def baixa_estoque(busca, produtos):
    clear()
    for num in busca:
        print(f'ID produto: {num}')
        print('produto:', produtos[num]['nome'])
        print('Quantidade em estoque: ', produtos[num]['qtd_estoque'])
        print('---' * 12)

    id_produto = int(input('Digite o ID do produto a ser editado:\n> '))
    qtd = int(input('Digite a quantidade que será dado baixa em estoque:\n> '))

    produtos[id_produto]['qtd_estoque'] -= qtd
    print('Dado baixa com sucesso!')


def opcoes_carrinho(carrinho, produtos):
    clear()
    menu = tela_carrinho()
    opcao = int(input(menu))

    while opcao != 0:
        clear()
        if opcao == 1:
            mostrar_carrinho(carrinho, produtos)

        elif opcao == 2:
            remover_item_carrinho(carrinho)

        elif opcao == 3:
            efetuar_compra(carrinho, produtos)

        else:
            print('Opção inválida!\n')

        input('\n<enter> to continue...')
        opcao = int(input(menu))


def mostrar_carrinho(carrinho, produtos):
    clear()
    if len(carrinho) == 0:
        print_warning('Carrinho vazio!')
        return

    for item in carrinho:
        print_detalhes(item)

    print('\nGerenciar: 1')
    print('Voltar: 0')
    opcao = int(input('> '))

    if opcao == 1:
        opcoes_carrinho(carrinho, produtos)


def remover_item_carrinho(carrinho):
    clear()
    cont = 0
    for item in carrinho:
        print(f'ID: {cont}')
        print_nome_marca(item)
        cont += 1

    sku = int(input('Digite o ID do item a ser removido\n> '))
    del carrinho[sku]


# Fazer a opção de efetuar a compra
def efetuar_compra(carrinho, produtos):
    clear()

    valor_total = 0
    for item in carrinho:
        if item in produtos:
            print('\n' + item['nome'])
            qtd = int(input('Quantidade a ser comprada: '))
            valor_total += item['valor'] * qtd
            
    print_warning(f'Confirmar a compra no valor de {valor_total}? (S/N)')
    opcao = input('> ')
    
    if opcao == 'S':
        print_success('MUITO OBRIGADO!')
        carrinho.clear()
        input('')
        clear()
        tela_cliente(produtos, carrinho)


def pesquisa_nome(produtos):
    clear()
    id_produto = 0
    busca = []
    print('Pesquisar por nome\n')
    pesquisa = input('Buscar: ').upper()
    for produto in produtos:
        if pesquisa in produto['nome'].upper():
            print_nome_marca(produto)
            busca.append(id_produto)
        id_produto += 1

    return busca


def pesquisa_marca(produtos):
    clear()
    id_produto = 0
    busca = []
    print('Pesquisar por marca\n')
    pesquisa = input('Buscar: ').upper()

    for produto in produtos:
        if pesquisa in produto['marca'].upper():
            print_nome_marca(produto)
            busca.append(id_produto)
        id_produto += 1

    return busca


def pesquisa_categoria(produtos):
    clear()
    id_produto = 0
    busca = []
    print('Pesquisar por categoria\n')
    pesquisa = input('Buscar: ').upper()
    for produto in produtos:
        if pesquisa in produto['categoria'].upper():
            print_nome_marca(produto)
            busca.append(id_produto)
        id_produto += 1

    return busca


def inicializar(nome_arquivo):
    produtos_carregados = []
    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        dados = arquivo.readline()
        arquivo.close()
        produtos_carregados = json.loads(dados)

    return produtos_carregados


def salvar(nome_arquivo, produtos):
    dados = json.dumps(produtos)
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)


def finalizar(nome_arquivo, produtos):
    dados = json.dumps(produtos)
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)
    arquivo.close()


def autenticar(usuarios):
    print_info('---- LOGIN ----')
    email = input('Email: ')
    senha = getpass.getpass('Senha: ')

    return UserAuth(usuarios).auth(email, senha)


if __name__ == '__main__':
    App.init()
    main()
