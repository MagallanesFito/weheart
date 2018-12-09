from webapp.models import Interest

#Se cargan los hobbies en espanol
def procesar(cadena):
	procesada = str(cadena).title()
	resumida = procesada.split("(")[0]
	resumida = resumida.split(":")[0]
	result = resumida
	if resumida[-1] == ' ':
		result = resumida[:-1]
	if result[-1] != '\n':
		result+='\n'
	return result
hobbies_list = []
file = open("hobbies_spanish.txt",'r')
for line in file:
	procesado = procesar(line)
	if procesado not in hobbies_list:
		hobbies_list.append(procesado)
#hobbies en ingles
file.close()
file = open("hobbies.txt",'r')
for line in file:
	procesado = procesar(line)
	if procesado not in hobbies_list:
		hobbies_list.append(procesado)
file.close()

#La lista debe mostrar los hobbies ordenados para facilitar la busqueda
file = open("hobbies_list.txt",'w')
hobbies_list.sort()
for hobbie in hobbies_list:
	file.write(hobbie)
	p = Interest(name=str(hobbie))
	p.save()
file.close()