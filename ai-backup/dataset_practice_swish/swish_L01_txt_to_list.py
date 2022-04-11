txt_file = 'food_classes_swish.txt'

eng_label_list = []

with open(txt_file, 'r', encoding='UTF-8') as f:
    lines = f.read().splitlines()
    for line in lines:
        # print(line)
        eng_label_list.append(line)
print(eng_label_list)
