import random

pessoas1 = [
    "Henrique Nogueira Pedro Lindoso",
    "Gabriel Grub Vidal da Silva",
    "Fernanda Mees Antunes",
    "André Menniti Pennini",
]
pessoas0 = [
    "Adriel Faustino de Oliveira",
    "Amanda Emi Yamasaki",
    "Ana Werneck de Souza Dias",
    "Felipe de Souza Lourenço",
    "Fernanda Mayumi Sakamoto Iizuka",
    "Guilherme Vinicius Afonso Dias de Freitas",
    "Kim Ju Hyang",
    "Leticia Amy Siramidu",
    "Marcelo Tamay Honda",
    "Maria Dulce Navarro de Britto Matos",
    "Mateus Pamio Forcione de Oliveira e Souza",
    "Milena da Silva Ramos",
    "Paulo Sergio Almeida de Oliveira",
    "Theo Borten Radesca Migliano",
    "Vitor Tatiama Gouveia",
]
i = 0
grupo1 = []
while i < 4:
    x = random.choice(pessoas0)
    grupo1.append(x)
    pessoas0.remove(x)
    i = i + 1
x = random.choice(pessoas1)
grupo1.append(x)
pessoas1.remove(x)

grupo2 = []
i = 0
while i < 4:
    x = random.choice(pessoas0)
    grupo2.append(x)
    pessoas0.remove(x)
    i = i + 1
x = random.choice(pessoas1)
grupo2.append(x)
pessoas1.remove(x)

grupo3 = []
i = 0
while i < 4:
    x = random.choice(pessoas0)
    grupo3.append(x)
    pessoas0.remove(x)
    i = i + 1
x = random.choice(pessoas1)
grupo3.append(x)
pessoas1.remove(x)

grupo4 = pessoas0 + pessoas1
print(f"Os integrantes do grupo 1 são: {', '.join(grupo1)}")
print(f"Os integrantes do grupo 2 são: {', '.join(grupo2)}")
print(f"Os integrantes do grupo 3 são: {', '.join(grupo3)}")
print(f"Os integrantes do grupo 4 são: {', '.join(grupo4)}")
