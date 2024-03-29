# #Usando a função open para criar um objeto do tipo arquivo para leitura
# arquivo = open("C:\\Users\\Santi\\Pictures\\python\\arquivo_texto.txt")

# print(arquivo.read())

# #Lendo somente 50 bytes
# # print(arquivo.read(50))

# #lendo linha a linha
# print(type(arquivo.readlines()))

#linha a linha com loop
# for linha in arquivo.readlines():
#     print(linha.rstrip())

# linhasArquivo = arquivo.readlines()

# print(f"Ei, eu consegui tranformar meu arquivo em uma {type(linhasArquivo)}")

# linhasArquivo.sort()
# # print(linhasArquivo)

# for i in linhasArquivo:
#     print(i)

# linha = arquivo.readline()
# print(linha)

# palavras = linha.split()
# print(palavras)

# posicao = arquivo.tell()
# print(posicao)

# arquivo.close()

# #Usando a função open para criar um objeto do tipo arquivo para escrita
# arquivo = open("C:\\Users\\Santi\\Pictures\\python\\novo_texto.txt", "a")

# conteudo = "Estou testando novamente, agora vai"
# arquivo.write(conteudo)

# arquivo.close()

arquivo = open("C:\\Users\\Santi\\Pictures\\python\\aaa_texto.txt")
print(type(arquivo))
