def open_and_print_file_per_line(path):
	with open(path) as file:
		for line in file.readlines():
			print(f'Linea: {line}')

open_and_print_file_per_line('nombres de canciones.txt')

def create_and_print_file_alphabetic(path):
	with open(path) as file:
		song = file.readlines()
	song.sort()
	with open("canciones alfabeticamente2.txt", "w") as file:
		file.writelines(song)
	return "canciones alfabeticamente2.txt"

create_and_print_file_alphabetic("nombres de canciones.txt")

archivo_creado = create_and_print_file_alphabetic("nombres de canciones.txt")

with open(archivo_creado) as file:
	for line in file:
		print(f"Ordenado: {line.strip()}")
	
