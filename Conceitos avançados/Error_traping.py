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
	except:
		return None

print(reciprocal(0))

#Voce pode criar armadilhas para certos errinhos
try:
	print(reciprocal("valores_testes"))
except ZeroDivisionError:
	#Nesse caso pegamos o carinha que teve a ideia genial de dividir 0
	print("Voce tentou dividir por 0")
	#Nesse caso pegamo o carinha que decidiu se utilizar de strings
except TypeError:
	print("Voce e um batatas")
except:
	print("Voce e um super batata")
#Cuidado ao fazer isso daki pq voce fez uma bolinha de erro, isso daki so vai acontecer
# Se o user querer printar algo, especifico se utilizando da sua funcao. Ele e o que
#Vai ter que fazer isso.
