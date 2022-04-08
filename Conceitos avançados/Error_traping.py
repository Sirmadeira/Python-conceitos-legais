#Existe maneira de encontrar o seu erro.

def reciprocal(number:float) -> float:
	try:
		return(1/number)
	except ZeroDivisionError:
	#Nesse caso pegamos o carinha que teve a ideia genial de dividir 0
		print("Voce tentou dividir por 0")
		return None
	except TypeError:
		print("Voce e um batatas")
	#Excesao para certos erros
	except:
		raise Exception('Impossivel dividir 0')

print(reciprocal(0))

