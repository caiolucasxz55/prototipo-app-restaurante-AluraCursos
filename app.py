import os

restaurantes = [{'nome':'bella napoli', 'categoria':'pizzaria' ,'ativo':'false'},
                {'nome': 'oue', 'categoria':'sushi', 'ativo':'true'}
                ]

def sair_do_app():
    os.system('cls')
    print('saindo da aplicaçao')



def exibir_nome_do_programa():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def menu_itens():
    print('-'*40)
    print('[1]- Cadastrar Restaurante')
    print('[2]- Exibir Restaurantes Cadastrados')
    print('[3]- Ativar Restaurante')
    print('[4]- Sair')
    print('-'*40)
    print('\n')

def cadastrar_restaurante():
    nome_restaurante = input('Qual o nome do restaurante?: ')
    categoria = input(f'qual a categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso')
    input('digite algo para voltar ao menu: ')
    os.system('cls')
    main()
    
def listar_restaurantes():
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        atividade_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | - {categoria_restaurante.ljust(20)} | - {atividade_restaurante}')   
    input('digite algo para voltar ao menu: ')
    main()

def ativar_restaurante():
    nome_restaurante = input(' digite o nome do restaurante que quer ativar: ')
    
    for restaurante in restaurantes:
        restaurante_encontrado = True
        if restaurante == restaurante['nome']:
            restaurante['ativo'] = not restaurante ['ativo']
            print(f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso')
            input('digite algo para voltar ao menu: ')
            main()
    if not restaurante_encontrado:
        print(' o restaurante n foi encontrado')








def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opçao: '))

    if opcao_escolhida == 1:
        os.system('cls')
        print('Indo para o cadastro')
        cadastrar_restaurante()
    elif opcao_escolhida == 2:
        os.system('cls')
        print('Exibindo Restaurantes')
        listar_restaurantes()
    elif opcao_escolhida == 3:
        os.system('cls')
        print('Indo para Ativaçao')
        ativar_restaurante()
    elif opcao_escolhida == 4:
        sair_do_app()
    else:
        print('digite um numero valido ')
        input('digite algo para voltar ao menu principal: ')
        os.system('cls')
        main()
        
        
def main():
        os.system('cls')
        exibir_nome_do_programa()   
        menu_itens()
        escolher_opcoes()
    
if __name__ == '__main__':
    main()

