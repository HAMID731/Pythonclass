input_list = [
    "x o x",
    "x x o",
    "x o o"
]

output_list = []

for item in input_list:
    output_list.append(item.replace("x", "|"))


for line in output_list:
    print(line)

