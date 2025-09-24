import json



def get_json_argument(json_data, key_path):
    """
    Récupère une valeur depuis un dictionnaire JSON en utilisant une liste de clés et/ou d'indices.
    Exemple:
        get_json_argument(data, ["inputs", 0, "type"])
    """
    value = json_data
    for key in key_path:
        if isinstance(value, dict):   # si c’est un dictionnaire
            value = value.get(key)
        elif isinstance(value, list) and isinstance(key, int):  # si c’est une liste
            if 0 <= key < len(value):
                value = value[key]
            else:
                return None
        else:
            return None
        if value is None:
            return None
    return value


def create_page(file_path):
    with open(file_path, "w") as f:
        f.write("#created by script\n")
        f.write("\n")


def add_library(file_path, name_class, inputs, outputs):
    with open(file_path, "a") as f:
        f.write("#include <iostream>\n")
        f.write("#include <boost/multiprecision/cpp_int.hpp>\n")
        f.write(f'#include "includes/{name_class}.hpp"\n\n')
        for i in range(len(inputs)):
            f.write(f'#include "includes/{inputs[i][0]}.hpp"\n')


# TODO :  Même fonction, à rassembler en une seule plus tard

def get_list_inputs(json_data, number_inputs):
    list_inputs = []
    for i in range(number_inputs):
        input_name = get_json_argument(json_data, ["inputs", i + 1, "name"])
        input_type = get_json_argument(json_data, ["inputs", i + 1, "Qbits"])
        list_inputs.append((input_name, input_type))
    return list_inputs

def get_list_outputs(json_data, number_outputs):
    list_outputs = []
    for i in range(number_outputs):
        output_name = get_json_argument(json_data, ["outputs", i + 1, "name"])
        output_type = get_json_argument(json_data, ["outputs", i + 1, "Qbits"])
        list_outputs.append((output_name, output_type))
    return list_outputs

def write_stimulis(name, type, stimuli, path = "includes/"):
    file_path = path + name + ".hpp"
    with open(file_path, "w") as f:
        f.write("// Created by script\n \n")
        f.write(f"#ifndef {name.upper()}_HPP\n")
        print(f"{name.upper()}_Stimuli created...")
        f.write(f"#define {name.upper()}_HPP\n \n")
        f.write("#include <iostream>\n")
        f.write("#include <boost/multiprecision/cpp_int.hpp>\n \n")
        f.write("using namespace boost::multiprecision;\n")
        f.write("template <int N>\n")
        f.write(f"using uint{type}_t = boost::multiprecision::number<boost::multiprecision::cpp_int_backend<{type}, {type}, boost::multiprecision::unsigned_magnitude, boost::multiprecision::unchecked, void>>;\n")
        f.write("\n\n")
        f.write(f"static const uint{type}_t {name}_stimuli[] = {{\n")
        for i in range(len(stimuli)):
            f.write(f"    {stimuli[i]},\n")
        f.write("};\n\n")
        f.write(f"#endif // {name.upper()}_HPP\n")
    return

# using uintN_t = boost::multiprecision::number<boost::multiprecision::cpp_int_backend<N, N, boost::multiprecision::unsigned_magnitude, boost::multiprecision::unchecked, void>>;


def get_stimuli(json_data, number_inputs, list_input):
    list_out = []
    for i in range(number_inputs):
        list_out.append(get_json_argument(json_data, [f"{list_input[0]}", "stimuli", i]))
    return list_out


def create_tb(json_data, path, name_component, list_inputs):
    for i in range(len(list_inputs)):
        list_stimuli = []
        nb_input = get_json_argument(json_data, [f"{list_inputs[i][0]}", "nb_stimuli"])
        list_stimuli = get_stimuli(json_data, nb_input, list_inputs[i])
        write_stimulis(list_inputs[i][0], list_inputs[i][1], list_stimuli, "includes/")

        




# print(get_json_argument(json_data, ["inputs", 0, "number"]))
# print(get_json_argument(json_data, ["outputs", 1, "name"]))
# print(get_json_argument(json_data, ["inputs", 2, "type"]))

# TODO : ne pas oubler de créer les références dans le main pour les différents TB

FILE_PATH = "main.cpp"
JSON_PATH = "config.json"
PATH = ""

if __name__ == "__main__":
    with open(JSON_PATH, "r") as f:
        JSON_DATA = json.load(f)
    NAME_COMPONENT = get_json_argument(JSON_DATA, ["name"])
    NB_INPUTS = get_json_argument(JSON_DATA, ["inputs", 0, "number"])
    NB_OUTPUTS = get_json_argument(JSON_DATA, ["outputs", 0, "number"])
    create_page(FILE_PATH)
    INPUT_DATA = get_list_inputs(JSON_DATA, NB_INPUTS)
    OUTPUT_DATA = get_list_outputs(JSON_DATA, NB_OUTPUTS)
    add_library(FILE_PATH, NAME_COMPONENT, INPUT_DATA, OUTPUT_DATA)
    create_tb(JSON_DATA, PATH, NAME_COMPONENT, INPUT_DATA)



















