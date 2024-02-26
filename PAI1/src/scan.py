import glob, os, hashlib, json, concurrent.futures

BUFFER_SIZE = 16384 # 16 kilo bytes

# Devuelve una lista de las rutas absolutas de todos los ficheros en el directorio especificado y todos sus sub-dicrectorios
# path: String -> directorio raíz a buscar
# only_hashes: Boolean -> decidir si sólo devolvemos los hashes
# print_hashes: Boolean -> pasa por la funcion dict_hashes
def scan_all_files(path, hashfunction, only_hashes, print_hashes):
    print("in scan all files function")
    # dependiente de tu sistema operativo es "\**" o "/**"
    path = path + "/**"
    filenames = []
    for filename in glob.iglob(path, recursive=True):
        if os.path.isfile(filename):  # filtrar dirs
            filenames.append(os.path.abspath(filename))

    dict_hashes = hash_all_files(filenames, hashfunction, print_hashes)
    if only_hashes:
        return dict_hashes
    else:
        return filenames


# Devuelve un dicionario de todos los hash de las rutas de los ficheros en la lista especificada a base de una función de hash y los guarda en hashes.json
# list_filenames: [] String -> lista con las rutas de los ficheros
# hashfunction: String -> especifica la función de hash
# print_hashes: Boolean -> decidir si guardamos los hashes en hashes.json
def hash_all_files(list_filenames, hashfunction, print_hashes):
    print("Hashing all files... Please wait!")
    dict_hashes = {}
    dict_hashes["hashes"] = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # función para calcular los hashes
        def calculate_hash(filename):
            bytes_file = read_file(filename)
            if hashfunction == "md5":
                dict_hashes["hashes"][filename] = hashlib.md5(bytes_file).hexdigest()
            elif hashfunction == "sh1":
                dict_hashes["hashes"][filename] = hashlib.sha1(bytes_file).hexdigest()
            else:
                dict_hashes["hashes"][filename] = hashlib.sha256(bytes_file).hexdigest()

        # calcular los valores de hash con multithreading
        executor.map(calculate_hash, list_filenames)

    if print_hashes:
        with open("hashes.json", "w") as write_file:
            json.dump(dict_hashes, write_file, indent=4)

    return dict_hashes

# Lee un fichero y devuelve los bytes
# file: String -> ruta del fichero a leer
def read_file(file):
    b = b""
    with open(file, "rb") as f:
        while True:
            # lee 16mil bytes del fichero
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # si no, terminamos
                break
            # si hay bytes, añadelos
            b += bytes_read       
    return b

# Lee el fichero hashes.json y devuelve el dicionario con la ruta como clave y el hash como valor
def read_hashes_to_dict():
    with open("hashes.json", "r") as read_file:
        dict_hashes = json.load(read_file)
    
    # print("\n".join("{0} |||| {1}".format(k, v)  for k,v in dict_hashes["hashes"].items()))
    return dict_hashes["hashes"]
