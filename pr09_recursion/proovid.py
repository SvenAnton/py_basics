name = "Sven"

new_name = ""

for index in range(len(name)):
    new_name += name[index - 1 - 2 * index]

print(new_name)
