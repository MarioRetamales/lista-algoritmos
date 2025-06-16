import re
from datetime import datetime

def apresenteSe():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| [SEUS NOMES E RAs AQUI]                                     |')
    print('|                                                             |')
    print('| Versão 2.0 de 26/05/2025                                    |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto(solicitacao, mensagem, valido):
    digitouDireito = False
    while not digitouDireito:
        txt = input(solicitacao)
        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            digitouDireito = True
    return txt

def opcaoEscolhida(mnu):
    print()
    opcoesValidas = []
    for posicao, item in enumerate(mnu):
        print(f"{posicao + 1}) {item}")
        opcoesValidas.append(str(posicao + 1))
    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

def ondeEsta(nom, agd):
    if len(agd) == 0:
        return [False, 0]
    inicio = 0
    final = len(agd) - 1
    while inicio <= final:
        meio = (inicio + final) // 2
        nome_meio = agd[meio][0].lower()
        nome_procurado = nom.lower()
        if nome_meio == nome_procurado:
            return [True, meio]
        elif nome_meio < nome_procurado:
            inicio = meio + 1
        else:
            final = meio - 1
    return [False, inicio]

def nomeValido(nome):
    return nome.replace(" ", "").isalpha()

def dataValida(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False     

def telefoneValido(telefone):
    return re.fullmatch(r"\d{8,10}", telefone) is not None

def celularValido(celular):
    return re.fullmatch(r"\d{9,11}", celular) is not None

def emailValido(email):
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", email) is not None

def enderecoValido(endereco):
    if len(endereco.strip()) < 10:
        return False
    if not re.search(r"[A-Za-z]", endereco):
        return False
    if not re.search(r"\d", endereco):
        return False
    return True

def cadastrar(agd):
    print("\n=== CADASTRAR NOVO CONTATO ===")
    while True:
        nome = input("Digite o nome do contato (ou 'cancela' para desistir): ").strip()
        if nome.lower() == 'cancela':
            print("Cadastro cancelado!")
            return
        if not nomeValido(nome):
            print("Nome inválido! Não use números ou símbolos.")
            continue
        resultado = ondeEsta(nome, agd)
        if resultado[0]:
            print(f"Erro: O contato '{nome}' já está cadastrado!")
            continue
        break

    while True:
        aniversario = input("Aniversário (dd/mm/aaaa): ").strip()
        if dataValida(aniversario):
            break
        print("Data inválida! Tente novamente.")


    while True:
        endereco = input("Endereço: ").strip()
        if enderecoValido(endereco):
            break
        print("Endereço inválido! Tente novamente.")

    while True:
        telefone = input("Telefone fixo (apenas números): ").strip()
        if telefoneValido(telefone):
            break
        print("Telefone inválido! Tente novamente.")

    while True:
        celular = input("Celular (apenas números): ").strip()
        if celularValido(celular):
            break
        print("Celular inválido! Tente novamente.")

    while True:
        email = input("E-mail: ").strip()
        if emailValido(email):
            break
        print("E-mail inválido! Tente novamente.")

    contato = [nome, aniversario, endereco, telefone, celular, email]
    agd.insert(resultado[1], contato)
    print(f"\n✓ Contato '{nome}' cadastrado com sucesso!")

# Demais funções (procurar, atualizar, listar, excluir, etc.) podem ser mantidas conforme o original

# Programa principal
def main():
    apresenteSe()
    agenda = []
    menu = ['Cadastrar Contato', 'Procurar Contato', 'Atualizar Contato', 'Listar Contatos', 'Excluir Contato', 'Sair do Programa']
    deseja_terminar_o_programa = False
    while not deseja_terminar_o_programa:
        opcao = int(opcaoEscolhida(menu))
        if opcao == 1:
            cadastrar(agenda)
        elif opcao == 6:
            deseja_terminar_o_programa = True
        else:
            print("Função ainda não implementada.")
    print('PROGRAMA ENCERRADO COM SUCESSO!')

if __name__ == "__main__":
    main()
