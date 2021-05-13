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


def pattern_search(sequence, pattern):
    """

    :param sequence:
    :param pattern:
    :return:
    """

    width = len(pattern)
    left_end = 0
    my_set = {}
    my_set = set(my_set)
    right_end = left_end + width

    while right_end < len(sequence):
        for idx_p in range(width):
            if pattern[idx_p] != sequence[left_end + idx_p]:
                break
        else:
            position = left_end + width // 2
            my_set.add(position)

        left_end += 1
        right_end += 1

   # while n < len(sequence) - width:
   #     seq_pattern = sequence[left_end:left_end+width]
   #     if seq_pattern == pattern:
   #         position = left_end + width // 2
   #         my_set.add(position)
   #     n += 1
   #     left_end += 1

    return my_set


def main():
    file_name = 'sequential.json'
    seq = read_data(file_name, "unordered_numbers")
    dict = linear_search(seq, 0)
    seq = read_data(file_name, 'dna_sequence')
    my_set = pattern_search(seq, 'ATA')

    print(my_set)


if __name__ == '__main__':
    main()
