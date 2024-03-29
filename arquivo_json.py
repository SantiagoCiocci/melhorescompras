import json

# contatos =  {
#     "Clark Kent":{
#        "Celular":"123456",
#        "Email":"super@krypton.com"
#     },
#     "Bruce Wayne":{
#        "Celular":"654321",
#        "Email":"bat@caverna.com.br"
#     }
#  }

# final = json.dumps(contatos, indent = 4)

# print(final)

# arquivo = open('C:\\Users\\Santi\\Pictures\\python\\agenda.json', 'w')

# arquivo.write(final)

# arquivo.close()

arquivo = open('C:\\Users\\Santi\\Pictures\\python\\agenda.json')

conteudo_arquivo = arquivo.read()

agenda = json.loads(conteudo_arquivo)

arquivo.close()

print(agenda)