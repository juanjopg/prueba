#elimina numero repitos
numeros=[1,3,67,67,8,8,5,9,5,3,0,12,12,23,45]

numeros = list(set(numeros))

print numeros


#elimina numero repetidos que esten seguidos
numero = [1,3,67,67,8,8,5,9,5,3,0,12,12,23,45]
for elemento in numero:
	posicion =numero.index(elemento)
	if posicion != len(numero) -1:
		if elemento == numero[posicion + 1]:
			numero.remove(elemento)
print numero

