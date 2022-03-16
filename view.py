import re
from controller import ControllerCadastro, ControllerLogin

while True:
    print('\n========== [MENU] ==========')
    decisao = input('''Digite para

    Cadastrar [1]
    Logar[2]
    Sair [3]
    
    :''')

    if decisao == '1':
        nome = input('\nNome:\n')
        email = input('\nE-mail:\n')
        senha = input('\nSenha (6 caracteres):\n')
        
        resultado = ControllerCadastro.cadastrar(nome, email, senha)

        if resultado == 2:
            print('\nTamanho do nome inválido.')
        elif resultado == 3:
            print('\nE-mail maior que 200 caracteres.')
        elif resultado == 4:
            print('\nTamanho da senha inválido.')
        elif resultado == 5:
            print('\nE-mail já cadastrado.')
        elif resultado == 6:
            print('\nErro interno do sistema.')
        elif resultado == 1:
            print('\nCadastro realizado com sucesso.')

    elif decisao == '2':
        email = input('\nE-mail: ')
        senha = input('Senha: ')
        
        resultado = ControllerLogin.login(email, senha)
    
        if not resultado:
            print('\nE-mail e/ou senha incorretos.')
        else:
            print(resultado)

    elif decisao == '3':
        print('\nSaindo...')
        break
    else:
        print('\nDigite um valor válido.')