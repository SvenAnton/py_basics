with open("hobbies_database.txt", 'r') as file:
    file_list = []
    for line in file:
        file_list.append(line)

name_set = set()
for i in file_list:
    name = i.split(":")[0]
    name_set.add(name)


name_list = list(name_set)

file_dict = {}
for name in name_list:
    dict_key = name
    dict_value = set()
    for line in file_list:
        if line.split(":")[0] == name:
            dict_value.add(line.split(":")[1].rstrip())
    file_dict[dict_key] = list(dict_value)

sorted(file_dict)


for keyy,vall in sorted(file_dict.items()):
    print(f"{keyy}, {'-'.join(sorted(vall))}")


print()




hobbies_list = []
for item in file_dict.values():
    for i in item:
        hobbies_list.append(i)

hobbies_set = set(hobbies_list)
hobbies_set_list = list(hobbies_set)

hobbies_dict = {}
for hb in hobbies_set_list:
    hobbies_dict[hb.rstrip()] = hobbies_list.count(hb)

print(hobbies_dict)






max_or_min_value = max(hobbies_dict.values(), default=None)

print()
print("K6ige populaarsemad on:")
for name in hobbies_dict:
    if hobbies_dict[name] == max_or_min_value:
        print(name)



















