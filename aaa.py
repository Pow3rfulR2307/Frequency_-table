import csv 
from math import log, ceil

def mostrar_dados(dados):
    for coluna in dados:
        print(coluna)

def mostrar_coluna(dados):

    posicao = int(input("0.X - 1.Y - 2.month - 3.day - 4.FFMC - 5.DMC - 6.DC - 7.ISI\n8.Temp - 9.RH - 10.Wind - 11.Rain - 12.Area:\n"))

    if posicao not in range(0, 13):
        print("Coluna Inválida")

    else:    
        print("\n---")
        for coluna in dados:
            print(coluna[posicao])
        print("---\n")

def ocorrencias(inicio, fim, lista):

    c = 0
    for i in lista:
        if i >= inicio and i<fim:
            c+=1
    return c

def intv(comeco, fim):

    i = []

    for x in range(0,11):
        i.append(comeco+ fim*x)

    return i

def criar_tabela(dados):

    selecao = int(input("0.X - 1.Y - 4.FFMC - 5.DMC - 6.DC - 7.ISI\n8.Temp - 9.RH - 10.Wind - 11.Rain - 12.Area:\n"))
    if selecao not in range(0,13) or selecao == 2 or selecao == 3:
        print("valor inválido")
    else:

        lista = []
        Fi = 0

        for coluna in dados:
            lista.append(float(coluna[selecao]))
 
        print(f"--------\nMinimo : {min(lista)} --- Máximo: {max(lista)}")

        print(f"Amplitude Total: {max(lista) - min(lista)}")

        print(f"Quantidade de Classes: {ceil(1 + 3.3*(log(len(lista))/log(10)))}")

        aplt = ceil((max(lista) - min(lista)) / (ceil(1 + 3.3*(log(len(lista))/log(10)))))

        print(f"Amplitude de Cada classe {aplt}")

        lista_i = intv(min(lista), aplt)

        print("|I| Intervalo        | fi | Xi | Fi |") 
        for x in range(10):
            Fi+=ocorrencias(lista_i[x], lista_i[x+1], lista)
            print(f"|{x+1}| {lista_i[x]} |--- {lista_i[x+1]}  | {ocorrencias(lista_i[x], lista_i[x+1], lista)} | {(lista_i[x]+lista_i[x+1])/2} | {Fi} |")

if __name__ == "__main__":

    dados = []
    with open('/path/to/csvfile.csv') as arquivo: 
        
        header = next(arquivo) 
        leitor = csv.reader(arquivo)

        for entrada in leitor:
            dados.append(entrada)
    
    while True:

        opcao = int(input("-----\n1.Mostrar Dados - 2. Mostrar coluna - 3.criar_tabela de variável(só numéricos) - 4. sair:\n"))

        if opcao == 1:
            mostrar_dados(dados)
        elif opcao == 2:
            mostrar_coluna(dados)
        elif opcao == 3:
            criar_tabela(dados)
        else:
            break
