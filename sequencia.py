def sequencia( posicao ) :
	res = ""
	
	repetir = posicao[0]
	posicao = posicao[1:]+" "
	x = 1
		
	for a in posicao:
		if a != repetir:
			res += str(x)+repetir
			x = 1
			repetir = a
		else:
			x += 1
	return res

num = "1"
inputn = input('Digite a posição: ')
if int(inputn) <= 0:
	print('Número inválido')
else:
	inputnf = int(inputn) - 1

	for i in range(int(inputnf)):
		num = sequencia(num)
	print(num)