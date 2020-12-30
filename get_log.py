import os
import pandas as pd


def log_parse(file_path):
    all_tmp = []
    tmp = []
    with open(file_path, 'r') as log:
        for line in log:
            if line == '[START]\n':
                tmp = []
            elif line == '[END]\n':
                all_tmp.append(tmp)
            else:
                first = int(line.split()[0].split('(')[1].split(',')[0])
                second = int(line.split()[1].split(')')[0])
                tmp.append((first, second))

    return all_tmp


def get_log():

    alphabet = {
        'A': 3,
        'B': 2,
        'C': 1,
        'D': 2,
        'E': 4,
        'F': 3,
        'G': 2,
        'H': 3,
        'I': 3,
        'J': 2,
        'K': 3,
        'L': 1,
        'M': 4,
        'N': 3,
        'O': 1,
        'P': 2,
        'Q': 2,
        'R': 3,
        'S': 1,
        'T': 2,
        'U': 1,
        'V': 2,
        'W': 4,
        'X': 2,
        'Y': 3,
        'Z': 3
    }

    alphabet_data = []

    for ab in alphabet.keys():
        path = './log/' + ab
        log_list = os.listdir(path)
        for log_path in log_list:
            abs_log_path = path + '/' + log_path
            parse_log = log_parse(abs_log_path)
            alphabet_data.append([ab, parse_log])

    alphabet_data = pd.DataFrame(alphabet_data)

    # Check Strobe Number
    check_data = []
    for data in alphabet_data.values.tolist():
        if(alphabet[data[0]] == len(data[1])):
            check_data.append(data)
    alphabet_data = pd.DataFrame(check_data)

    alphabet_data.to_json('alphabet_strobe.json')
