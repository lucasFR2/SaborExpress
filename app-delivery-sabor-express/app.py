import os

restaurantes = [{"nome":"Praça", "categoria":"Japonesa", "ativo":False}, {"nome":"Solar da Praça", "categoria": "Pizza", "ativo":True}, {"nome":"Golden Burguer", "categoria": "Hamburguer", "ativo":False}]

def project_name():
    """Função para exibir o nome do Projeto"""

    print(""" 
    ██████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    """)

def exb_opc():
    """Função para exibir as opções que o usuário irá interagir"""

    print("""
    1 - Cadastrar Restaurante
    2 - Listar Restaurantes
    3 - Ativar/Desativar Restaurante
    4 - Sair
    """)

def finalizar_app(): 
    """Função para finalizar o programa"""

    exb_subtitulo("Encerrando o programa...")

def voltar_menu():
    """Função que retorna ao menu de opções depois de selecionar uma das opções"""

    input("\nAperte enter para voltar ao menu. ")
    main()

def opc_invalida():
    """Função que retorna Inválido quando o usuário use opções que não existem neste código"""

    print("Opção inválida!\n")
    voltar_menu()

def exb_subtitulo(texto):
    """Função que exibe um subtítulo depois de uma opção selecionada, com * em volta do subtítulo"""

    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar():
    """Função responsável por cadastrar um novo Restaurante."""

    exb_subtitulo("Cadastro de novos restaurantes\n")
    nome_restaurante = input("Digite o nome do restaurante: ")
    categoria = input(f"Digite o nome da Categoria do restaurante {nome_restaurante}: ")

    dados_restaurante = {"nome":nome_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_restaurante)

    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_menu()

def listar():
    """Função que lista todos os restaurantes cadastrados pelo usuário, ou já cadastrado antes."""

    exb_subtitulo("Lista de todos os restaurantes cadastrados:\n")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo_restaurante = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante.ljust(20)}")
    voltar_menu()

def alterar_estado():
    """Função que altera o estado do restaurante, estando ativado ou desativado"""

    exb_subtitulo("Mudando o estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encotrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encotrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            msg = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            print(msg)
    if not restaurante_encotrado:
        print("O restaurante não foi encontrado.")
    voltar_menu()

def escolher_opc():
    """Função que definimos o que cada opção do usuário irá fazer"""

    try:
        opc_escolhida = int(input("Digite a opção que deseja: ")) #input 'lê' a interação do usuário;

        if opc_escolhida == 1:
            cadastrar()
        elif opc_escolhida == 2:
            listar()
        elif opc_escolhida == 3:
            alterar_estado()
        elif opc_escolhida == 4:
            finalizar_app()
        else:
            opc_invalida()
    except:
        opc_invalida()

def main():
    """Função main onde todas as funções que são necessárias para aparecer na tela estão"""
    os.system("cls")
    project_name()
    exb_opc()
    escolher_opc()

if __name__ == '__main__':
    main()
