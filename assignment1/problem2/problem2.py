import sys

array_file_name = sys.argv[1]
array_file = open(array_file_name, 'r')

amount_of_integers = array_file.readline()
array_text = array_file.readline()

def make_list(array_text):
    array = []
    for i in array_text.split(" "):
        array.append(int(i))
    return array

array = make_list(array_text)

def merge(array):
    if len(array) > 1:
        midpoint = len(array) // 2
        left = array[midpoint:]
        right = array[:midpoint]
        
        #Reference variables for indexes
        ref1 = 0
        ref2 = 0
        ref3 = 0

        #recursively call function
        merge(left)
        merge(right)

        while True:
            if ref1 >= len(left) or ref2 >= len(right):
                break
            if left[ref1] >= right[ref2]: 
                array[ref3] = right[ref2] 
                ref2 = ref2 + 1
            else: 
                array[ref3] = left[ref1] 
                ref1 = ref1 + 1
            ref3 = ref3 + 1

        while True: 
            if ref1 >= len(left):
                break
            array[ref3] = left[ref1] 
            ref1 = ref1 + 1
            ref3 = ref3 + 1

        while True: 
            if ref2 >= len(right):
                break
            array[ref3] = right[ref2] 
            ref2 = ref2 + 1
            ref3 = ref3 + 1

merge(array)
for i in array:
    print(str(i), end=' ')
print()

sys.stdout = open("assignment1/problem2/my-output-2.txt", "w")
for i in array:
    print(str(i), end=' ')
print()

sys.stdout = sys.__stdout__
