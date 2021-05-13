import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:  # alebo file.keys():
        return None

    with open(file_path, 'r') as json_file:
        dictionary = json.load(json_file)
    seq = dictionary[field]
    return seq


def main():
    file_name = 'sequential.json'
    seq = read_data(file_name, "unordered_numbers")
    print(seq)


if __name__ == '__main__':
    main()
