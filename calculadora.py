print ('Bem vindo! ')
nome = input('Qual seu nome? ')
print ('Olá',nome)

op = int(input('1. Soma \n2. Subtração \n3. Multiplicação \n4. Divisão \nEscolha uma opcao: '))
num1 = float(input("Digite o primeiro valor a ser calculado: "))
num2 = float(input("Digite o seungo valor a ser calculado: "))

if op == 1:
	print ("Resultado: ", num1 + num2)
elif op == 2:
	print ("Resultado: ", num1 - num2)
elif op == 3:
	print ("Resultado: ",num1 * num2)
elif op == 4:
	print ("Resultado: ",num1 / num2)
else:
	print ("Encerrando")
