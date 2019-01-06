# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

current_answer =1
def multiply_array_elements (element_at_index, last_element_at_index) :
    premul =1
    postmul =1

    if (element_at_index != 0):
        temp_mul = 1
        for j in range (0,element_at_index):
            temp_mul = temp_mul * array_of_elements[j]
        premul = temp_mul

    if (element_at_index != last_element_at_index -1):
        temp_mul2 = 1
        for k in range (element_at_index + 1,last_element_at_index):
            temp_mul2 = temp_mul2 * array_of_elements[k]
        postmul = temp_mul2

    current_answer = premul * postmul
    final_array_of_elements.append(current_answer)

array_of_elements = [1,2,3,4,5]
final_array_of_elements = []
number_of_elements = len(array_of_elements)

if (number_of_elements==0):
    print("Length of array too short")

if (number_of_elements==1):
    final_array_of_elements = array_of_elements

for i in range (0,number_of_elements):
    current_element = array_of_elements[i]
    multiply_array_elements(i,number_of_elements)

print ("Final Array is : ")

print(final_array_of_elements)
