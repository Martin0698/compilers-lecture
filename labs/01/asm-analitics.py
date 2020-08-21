import sys



def main():

	print("Analisis de desamblado:")

	scriptPath =  sys.argv[1]

	Listafuncion = []

	Instruccion = {}

	with open(scriptPath) as file:

		for line in file:

			if line[0]=='0':

				words =  line.split(" ")



				Listafuncion.append(words)

			else:



				words = line.split("\t")



				if len(words)>2:

					insands = words[2].split(" ")

					if len(insands) >0:

						if insands[0] in Instruccion:

							Instruccion[insands[0]] = Instruccion[insands[0]]+1

						else:

							Instruccion[insands[0]] = 1



	print("\nNumero de instrucciones {0}:\n".format(len(Instruccion)))

	for ins in Instruccion:

		print("  {0}\t: ejecutado {1} veces ".format (ins, Instruccion[ins]))

	print("\n Numero de Funciones{0}:\n".format(len(Listafuncion)))

	for fun in  Listafuncion:

		print("  {0}".format( fun[1][1:-3] ), end='' )

		space =(10-len(fun[1][1:-3])) * ' '

		print(space, end='')

		print(": en la ubicacion: {0}".format(fun[0][-4:] ))



if __name__ == '__main__':

	main()
