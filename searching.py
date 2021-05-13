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


def linear_search(seqence, number):
    """

    :param seqence:
    :param number:
    :return:
    """

    index_list = []
    cetnost = 0
    seq_len = len(seqence)
    index = 0
    while index < seq_len:
        if seqence[index] == number:
            index_list.append(index)
            cetnost += 1
        index += 1

    dictionary = {'positions': index_list, 'count': cetnost}
    return dictionary


def main():
    file_name = 'sequential.json'
    seq = read_data(file_name, "unordered_numbers")
    dict = linear_search(seq, 0)
    print(dict)


if __name__ == '__main__':
    main()
