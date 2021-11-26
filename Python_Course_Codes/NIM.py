def computador_escolhe_jogada(n, m):
	r = 1
	p = n
	while r < m:
		p = p - 1
		if p % (m + 1) == 0:
			break
		else:
			r = r + 1
	jogadapc = r
	return jogadapc
def usuario_escolhe_jogada(n, m):
	jogada = int(input("Quantas peças retirar? "))
	while jogada > m or jogada <= 0 or jogada > n:
		print("Essa jogada é inválida! Tente novamente.")
		print()
		jogada = int(input("Quantas peças retirar? "))
	return jogada

def partida():
	print()
	n = int(input("Digite o número de peças na mesa: "))
	m = int(input("Digite o número máximo de peças a se retirar: "))
	while m <= 0 or n <= 0:
		print()
		print("Por favor, digite ambos maiores que zero!")
		n = int(input("Digite o número de peças na mesa: "))
		m = int(input("Digite o número máximo de peças a se retirar: "))

	if n % (m + 1) == 0:
		print()
		print("Você começa")
		print()
		while n != 0:
			jogada = int(usuario_escolhe_jogada(n, m))
			if (n == jogada and n == 1):
				n = n - jogada
				print()
				print("Você tirou uma peça.")
				print("Fim de jogo! Você ganhou!")
				usuvenc = True
				break
			else:
				if (n == jogada and n != 1):
					print()
					print("Você tirou",jogada,"peças.")
					print("Fim de jogo! Você ganhou!")
					usuvenc = True
					break
				else:
					n = n - jogada
					print()
					print("Você tirou",jogada,"peças da mesa.")
					print("Agora restam",n,"peças na mesa.")
					print()
			jogadapc = computador_escolhe_jogada(n, m)
			if (n == jogadapc and n == 1):
				n = n - jogadapc
				print()
				print("O computador tirou uma peça.")
				print("Fim de jogo! O computador ganhou!")
				compvenc = True
				break
			else:
				if (n == jogadapc and n != 1):
					print()
					print("O computador tirou",jogadapc,"peças.")
					print("Fim de jogo! O computador ganhou!")
					compvenc = True
					break
				else:
					n = n - jogadapc
					print()
					print("O computador tirou",jogadapc,"peças da mesa.")
					print("Agora restam",n,"peças na mesa.")
					print()
			
	else:
		print()
		print("Computador começa")
		print()
		while n != 0:
			jogadapc = computador_escolhe_jogada(n, m)
			if (n == jogadapc and n == 1):
				n = n - jogadapc
				print()
				print("O computador tirou uma peça.")
				print("Fim de jogo! O computador ganhou!")
				compvenc = True
				break
			else:
				if (n == jogadapc and n != 1):
					print()
					print("O computador tirou",jogadapc,"peças.")
					print("Fim de jogo! O computador ganhou!")
					compvenc = True
					break
				else:
					n = n - jogadapc
					print()
					print("O computador tirou",jogadapc,"peças da mesa.")
					print("Agora restam",n,"peças na mesa.")
					print()
			jogada = usuario_escolhe_jogada(n, m)
			if (n == jogada and n == 1):
				n = n - jogada
				print()
				print("Você tirou uma peça.")
				print("Fim de jogo! Você ganhou!")
				compvenc = False
				break
			else:
				if (n == jogada and n != 1):
					print()
					print("Você tirou",jogada,"peças.")
					print("Fim de jogo! Você ganhou!")
					compvenc = False
					break
				else:
					n = n - jogada
					print()
					print("Você tirou",jogada,"peças da mesa.")
					print("Agora restam",n,"peças na mesa.")
					print()
	return compvenc
def campeonato():
	x = 0
	y = 0
	print()
	print("Você escolheu um campeonato!")
	print()
	print("---- Rodada 1 ----")
	compvenc = partida()
	if compvenc == True:
		x = x + 1
		print()
		print("---- Rodada 2 ----")
		compvenc = partida()
		if compvenc == True:
			x = x + 1
			print()
			print("---- Rodada 3 ----")
			compvenc = partida()
			if compvenc == True:
				x = x + 1
				print()
				print("---- Final do campeonato! ----")
				print()
				print("Placar: Você",y,"X",x,"Computador")
			else:
				print("Impossível!")
		else:
			print("Impossível!")
	else:
		print("Impossível!")
print()
print("Bem vindo ao jogo NIM. Escolha:")
print()
print("1 - para jogar uma partida isolada")
esc = int(input("2 - para jogar um campeonato "))
while esc != 1 and esc != 2:
	int(input("Por favor, escolha 1 ou 2"))
if esc == 1:
	print()
	print("Você escolheu uma partida isolada!")
	partida()
else:
	campeonato()
	 