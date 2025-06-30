import re
from datetime import datetime

def apresenteSe():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Mário Retamales Giusti - RA: 25017542                       |')
    print('|                                                             |')
    print('| Versão 2.0 de 18/06/2025                                    |')
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
    posicao = 0
    while posicao < len(mnu):
        print(posicao + 1, ') ', mnu[posicao], sep='')
        opcoesValidas.append(str(posicao + 1))
        posicao += 1
    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)


def ondeEsta(nom, agd):
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
    return bool(re.fullmatch(r"[A-Za-zÀ-ÿ ]+", nome)) and nome.strip() != ""


def dataValida(data):
    # Aceita apenas formato dd/mm/aaaa e data até 2025
    try:
        dt = datetime.strptime(data, '%d/%m/%Y')
        if dt > datetime(2025, 12, 31):
            return False
        return True
    except:
        return False


def enderecoValido(endereco):
    # Precisa ter "Rua", "Avenida", "Travessa" ou "Estrada" e número
    tipos = ["rua", "avenida", "av.", "travessa", "estrada", "rodovia"]
    if not any(tp in endereco.lower() for tp in tipos):
        return False
    if not re.search(r"\d+", endereco):  # precisa ter pelo menos um número
        return False
    palavras = endereco.split()
    if len(palavras) < 3:  # Exige pelo menos: tipo + nome + número
        return False
    return True


def telefoneValido(telefone):
    # Só números, 8 a 10 dígitos, não pode ter letras
    return bool(re.fullmatch(r"\d{8,10}", telefone))


def celularValido(celular):
    # Só números, 9 a 11 dígitos, não pode ter letras
    return bool(re.fullmatch(r"\d{9,11}", celular))


def emailValido(email):
    # Tem que ter @, texto antes e depois, e pelo menos um ponto depois do @
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+", email))


def cadastrar(agd):
    while True:
        nome = input("Digite o nome do contato (ou 'cancela' para sair): ").strip()
        if nome.lower() == "cancela":
            print("Cadastro não realizado.")
            return
        if not nomeValido(nome):
            print("Nome inválido! Só letras e espaços são permitidos.")
            continue
        resultado = ondeEsta(nome, agd)
        if resultado[0]:
            print("Nome já cadastrado, tente outro.")
        else:
            break

    while True:
        aniversario = input("Aniversário (dd/mm/aaaa): ").strip()
        if not dataValida(aniversario):
            print("Data inválida! Formato deve ser dd/mm/aaaa, e não pode ser futura.")
        else:
            break

    while True:
        endereco = input("Endereço (ex: Rua das Flores 123): ").strip()
        if not enderecoValido(endereco):
            print("Endereço inválido! Tem que conter tipo, nome e número (ex: Rua das Flores 123).")
        else:
            break

    while True:
        telefone = input("Telefone fixo (apenas números, 8 a 10 dígitos): ").strip()
        if not telefoneValido(telefone):
            print("Telefone inválido! Só números, de 8 a 10 dígitos, sem letras.")
        else:
            break

    while True:
        celular = input("Celular (apenas números, 9 a 11 dígitos): ").strip()
        if not celularValido(celular):
            print("Celular inválido! Só números, de 9 a 11 dígitos, sem letras.")
        else:
            break

    while True:
        email = input("E-mail: ").strip()
        if not emailValido(email):
            print("E-mail inválido! Tem que conter @ e ponto, exemplo: email@dominio.com")
        else:
            break

    contato = [nome, aniversario, endereco, telefone, celular, email]
    agd.insert(resultado[1], contato)
    print(f"Cadastro de {nome} realizado com sucesso!")


def procurar(agd):
    if not agd:
        print("Agenda vazia.")
        return
    while True:
        nome = input("Digite o nome a procurar (ou 'cancela' para sair): ").strip()
        if nome.lower() == "cancela":
            print("Busca cancelada.")
            return
        resultado = ondeEsta(nome, agd)
        if resultado[0]:
            contato = agd[resultado[1]]
            print(f"\n--- Dados do contato ---")
            print(f"Nome: {contato[0]}")
            print(f"Aniversário: {contato[1]}")
            print(f"Endereço: {contato[2]}")
            print(f"Telefone: {contato[3]}")
            print(f"Celular: {contato[4]}")
            print(f"E-mail: {contato[5]}")
            return
        else:
            print("Nome não encontrado, tente novamente.")


def atualizar(agd):
    if not agd:
        print("Agenda vazia.")
        return
    while True:
        nome = input("Digite o nome do contato para atualizar (ou 'cancela' para sair): ").strip()
        if nome.lower() == "cancela":
            print("Atualização cancelada.")
            return
        resultado = ondeEsta(nome, agd)
        if resultado[0]:
            idx = resultado[1]
            contato = agd[idx]
            submenu = [
                'Aniversário',
                'Endereço',
                'Telefone',
                'Celular',
                'E-mail',
                'Finalizar atualizações'
            ]
            while True:
                print(f"\n--- Atualizar contato: {contato[0]} ---")
                op = int(opcaoEscolhida(submenu))
                if op == 1:
                    while True:
                        aniversario = input("Novo aniversário (dd/mm/aaaa): ").strip()
                        if not dataValida(aniversario):
                            print("Data inválida! Formato deve ser dd/mm/aaaa, e não pode ser futura.")
                        else:
                            contato[1] = aniversario
                            break
                elif op == 2:
                    while True:
                        endereco = input("Novo endereço: ").strip()
                        if not enderecoValido(endereco):
                            print("Endereço inválido! Tem que conter tipo, nome e número (ex: Rua das Flores 123).")
                        else:
                            contato[2] = endereco
                            break
                elif op == 3:
                    while True:
                        telefone = input("Novo telefone fixo: ").strip()
                        if not telefoneValido(telefone):
                            print("Telefone inválido! Só números, de 8 a 10 dígitos, sem letras.")
                        else:
                            contato[3] = telefone
                            break
                elif op == 4:
                    while True:
                        celular = input("Novo celular: ").strip()
                        if not celularValido(celular):
                            print("Celular inválido! Só números, de 9 a 11 dígitos, sem letras.")
                        else:
                            contato[4] = celular
                            break
                elif op == 5:
                    while True:
                        email = input("Novo e-mail: ").strip()
                        if not emailValido(email):
                            print("E-mail inválido! Tem que conter @ e ponto, exemplo: email@dominio.com")
                        else:
                            contato[5] = email
                            break
                elif op == 6:
                    print("Atualizações finalizadas.")
                    return
        else:
            print("Nome não encontrado, tente novamente.")


def listar(agd):
    if not agd:
        print("Não há contatos cadastrados.")
        return
    print("\n--- Lista de Contatos ---")
    for c in agd:
        print(f"Nome: {c[0]}, Aniversário: {c[1]}, Endereço: {c[2]}, Telefone: {c[3]}, Celular: {c[4]}, E-mail: {c[5]}")
    print("--- Fim da lista ---")


def excluir(agd):
    if not agd:
        print("Agenda vazia.")
        return
    while True:
        nome = input("Digite o nome a excluir (ou 'cancela' para sair): ").strip()
        if nome.lower() == "cancela":
            print("Exclusão cancelada.")
            return
        resultado = ondeEsta(nome, agd)
        if resultado[0]:
            idx = resultado[1]
            contato = agd[idx]
            print(f"\nEncontrado: Nome: {contato[0]}, Aniversário: {contato[1]}, Endereço: {contato[2]}, Telefone: {contato[3]}, Celular: {contato[4]}, E-mail: {contato[5]}")
            confirma = input("Confirma exclusão? (s/n): ").strip().lower()
            if confirma == "s":
                agd.pop(idx)
                print("Exclusão bem sucedida.")
                return
            else:
                print("Exclusão não realizada.")
                return
        else:
            print("Nome não encontrado, tente novamente.")


# Programa principal
apresenteSe()

agenda = []  # listona que conterá listinhas

menu = [
    'Cadastrar Contato',
    'Procurar Contato',
    'Atualizar Contato',
    'Listar Contatos',
    'Excluir Contato',
    'Sair do Programa'
]

deseja_terminar_o_programa = False
while not deseja_terminar_o_programa:
    opcao = int(opcaoEscolhida(menu))

    if opcao == 1:
        cadastrar(agenda)
    elif opcao == 2:
        procurar(agenda)
    elif opcao == 3:
        atualizar(agenda)
    elif opcao == 4:
        listar(agenda)
    elif opcao == 5:
        excluir(agenda)
    else:  # opcao == 6
        deseja_terminar_o_programa = True

print('PROGRAMA ENCERRADO COM SUCESSO!')
