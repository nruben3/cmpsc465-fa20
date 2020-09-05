import sys

array_file_name = sys.argv[1]
array_file = open(array_file_name, 'r')

array1_text = array_file.readline()
array2_text = array_file.readline()

def make_list(array_text):
    array = []
    for i in array_text.split(" "):
        array.append(int(i))
    return array

array1 = make_list(array1_text)
array2 = make_list(array2_text)

new_array = []

def place_in_array(new_array, number):
    placed = False
    index = 0
    while placed == False:
        if len(new_array) == index:
            new_array.append(number)
            placed = True
        elif len(new_array) == 1:
            if number >= new_array[index]:
                new_array.append(number)
            else:
                new_array.insert(index, number)
            placed = True
        elif index == 0:
            if number < new_array[index+1]:
                new_array.insert(index, number)
                placed = True
            else:
                index += 1
        else:
            if number <= new_array[index] and number > new_array[index-1]:
                new_array.insert(index, number)
                placed = True
            else:
                index += 1
    return new_array


def sort_lists():
    for i in array1[1:]:
        place_in_array(new_array, i)
    for i in array2[1:]:
        place_in_array(new_array, i)

sort_lists()
new_array.insert(0, len(new_array))

for i in new_array:
    print(str(i), end=' ')
print()

output_file_name = "assignment1/problem1/" + sys.argv[2]
sys.stdout = open(output_file_name, "w")
for i in new_array:
    print(str(i), end=' ')
print()

sys.stdout = sys.__stdout__



