#Para csv precisa importar a bliblioteca csv
import csv

# arquivo_csv = open('csv.csv', 'r')

# leitor_csv = csv.reader(arquivo_csv, delimiter=',', quotechar='"')

# next(leitor_csv)  # Ignora a primeira linha, que contém apenas os títulos das colunas

# for linha in leitor_csv:
#     mensagem = f"O Jedi de nome {linha[0]}, com {linha[1]} anos de idade, é classificado como {linha[2]}."
#     print(mensagem)

# arquivo_csv.close()

#Abrindo arquivo com o with
# with open('csv.csv', 'r') as arquivo_csv:
#     leitor_csv = csv.reader(arquivo_csv, delimiter=',', quotechar='"')

#     next(leitor_csv)  # Ignora a primeira linha, que contém apenas os títulos das colunas

#     for linha in leitor_csv:
#         mensagem = f"O Jedi de nome {linha[0]}, com {linha[1]} anos de idade, é classificado como {linha[2]}."
#         print(mensagem)

#Escrevendo em um arquivo csv
import csv

dados_jedi = ["Sant", "25", "Mestre"], ["Tsu", "29", "Mestre"]

with open('csv.csv', mode='a', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=',')
    for i in dados_jedi:
        escritor_csv.writerow(i)