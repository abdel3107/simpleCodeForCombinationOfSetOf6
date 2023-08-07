import random
from itertools import combinations

my_list = ['Karlin', 'Alain', 'Aristide', 'Ulrich', 'Karol', 'Abdel']

final_list = []

while len(final_list) < 8:

    random.shuffle(my_list)

    first_tuple = tuple(my_list[:3])

    second_tuple = tuple(my_list[3:])
    
    combined_tuple = (first_tuple, second_tuple)

    if combined_tuple not in final_list:
        final_list.append(combined_tuple)


if __name__ == '__main__':
    
    list_name = "combination"

    file_name = f"{list_name}.txt"

    with open(file_name, "w") as file:
        for item in final_list:
            file.write(str(item) + "\n")

    print(f"List '{list_name}' exported to '{file_name}'.")
