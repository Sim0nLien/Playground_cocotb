
# Créer le fichier et écrire des lignes dessus

def get_json_argument(json_data, key_path):
    """
    Récupère une valeur depuis un dictionnaire JSON en utilisant une liste de clés.
    Exemple d'utilisation:
        get_json_argument(data, ["settings", "timeout"])
    """
    value = json_data
    for key in key_path:
        value = value.get(key)
        if value is None:
            return None
    return value


def create_page(file_path):
    with open(file_path, "w") as f:
        f.write("#created by script\n")


def add_library(file_path, name_class):
    with open(file_path, "a") as f:
        f.write("#include <iostream>\n")
        f.write("#include <boost/multiprecision/cpp_int.hpp>")
        f.write(f'#include "includes/{name_class}.hpp')
        f.write("\n\n")

# Les Variables




file_path = "main.cpp"
json_path = "config.json"

if __name__ == "__main__":
    create_page(file_path)
    add_library(file_path, "adder")
    






