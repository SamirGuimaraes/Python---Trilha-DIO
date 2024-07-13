"""
Você foi designado para desenvolver um programa para gerenciar os 
equipamentos de uma empresa. O objetivo é criar um solução que permita 
aos usuários inserir informações sobre os equipamentos que serão 
cadastrados na rede, em seguida, exibir essa lista de equipamentos. 
Crie uma Lista para armazenar esses equipamentos e depois um loop 
para solicitar ao usuário inserir até três equipamentos.

Entrada
O programa solicitará ao usuário que insira uma lista com três 
equipamentos para adicionar a rede.
"""

itens = []

for i in range(3):
    item = input()
    itens.append(item)

print("Lista de Equipamentos:")
for item in itens:
    print(f"- {item}")