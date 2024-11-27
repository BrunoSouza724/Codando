import sqlite3

con = sqlite3.connect('Dados_Pessoais.db')
cursor = con.cursor()

nome = input("Informe o seu nome: ")
cpf = int(input("Informe o seu CPF: "))
idade = int(input("Informe a sua idade: "))

cursor.execute(
    'INSERT INTO Dados_Pessoais (nome, cpf, idade) VALUES (?, ?, ?)', (nome, cpf, idade))
con.commit()

print('Dados inseridos')