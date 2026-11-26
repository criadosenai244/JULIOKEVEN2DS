contato = {
    "nome": "Ana Souza",
    "telefone": "61 9999-0000",
    "email": "ana@gmail.com"
}

print(contato["telefone"])
print(contato["nome"])
contato["telefone"] = "61 9888-9999" # altera um valor existente
contato["cidade"] = "Taguatinga"     # adiciona um chave nova
del contato["email"]                 # remove a chave e o valor

print(contato)
