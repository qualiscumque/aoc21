data = []
with open("../input/input.txt") as f:
    data = [line.strip() for line in f.readlines() if line.strip()]


def transpose(in_data):
    width = len(in_data[0])
    out_data = []
    for x in range(0, width):
        num = ""
        for line in in_data:
            num += line[x]
        out_data.append(num)
    return out_data


def search_char(line, oxygen=None):
    if oxygen:
        return "1" if line.count("1") >= line.count("0") else "0"
    else:
        return "0" if line.count("1") >= line.count("0") else "1"


def filter_list(in_list, data_len, oxygen=None):
    for idx in range(data_len+1):
        new_transposed = transpose(in_list)
        search_val = search_char(new_transposed[idx], oxygen=oxygen)
        in_list = list(filter(lambda x: x[idx] == search_val, in_list))
        if len(in_list) == 1:
            return in_list

    return in_list


len_transposed = len(transpose(data))

oxygen_output = filter_list(data, len_transposed, True)
oxygen_val = int(oxygen_output[0], 2)

co2_output = filter_list(data, len_transposed)
co2_val = int(co2_output[0], 2)

print(f"ox:{oxygen_val} co2:{co2_val}")
print(f"result {oxygen_val * co2_val}")


