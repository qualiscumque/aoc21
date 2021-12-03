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
        num = ""
    return out_data

def gamma_rate(in_data):
    number = ""
    for line in in_data:
        number += "1" if line.count("1") > line.count("0") else "0"
    return int(number, 2)

def epsilon_rate(gamma):
    gamma_rate = "{0:b}".format(gamma)
    epsilon = ""
    for char in gamma_rate:
        epsilon += "0" if char is "1" else "1" 
    return int(epsilon, 2)

print(data)
out_data = transpose(data)
gamma = gamma_rate(out_data)
epsilon = epsilon_rate(gamma)

print(f"Gamma Rate: {gamma}")
print(f"Epsilon Rate: {epsilon}")
print(f"Result {gamma * epsilon}")
