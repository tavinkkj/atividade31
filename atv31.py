# Crie um programa que permita até 3 tentativas de login. 
# Se o usuário errar o nome ou senha três vezes, o acesso deve ser bloqueado e o programa exibirá “Usuário bloqueado por excesso de tentativas.”

nome = 'tavin'
senha = 210
tent = 3

for i in range(tent):
    nome_usuario = (input("Digite o nome: "))
    senha_usuario = int(input("Digite a senha: "))

if nome_usuario == nome and senha_usuario == senha:
    print("Acesso autorizado.")
else: 
    print("Usuário bloqueado por excesso de tentativas.")

