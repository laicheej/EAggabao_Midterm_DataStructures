'''
EDELAIZA JULIENNE AGGABAO BCS24
--------------------------------------------------------
Algorithm:
1. Create your 3x3 array and input the values needed
2. Create a function (FindingMax_Element) to store the task and call later. 
3. Initialize an empty value (max_element)
4. Iterate through each row in the array and compare the values.
5. For each row, find the maximum value in the row by using element > max_element
6. If the element is greater than the max element, store in element.
7. After iterating through all three rows, return the maximum value as the result. 
8. Call the function made earlier and print.

-------------------------------------------------------
Pseudocode:

Start
initialize my_array = [1,2,3]
                      [4,5,6]
                      [9.6,9.8,9.9]
function FindingMax_Element:
    max element = float
    Loop 1: for row in array
        Loop 2: for element in row
            if element > max_element
                max_element = element
        return max_element
print function Finding_Max of My_Array
Stop

'''

my_array = [[1,2,3],
            [4,5,6],
            [9.6,9.7,9.9]]

def FindingMax_Element(array): 
    max_element = float()
    for row in array:
       for element in row:
           if element > max_element:
               max_element = element
    return max_element
print(FindingMax_Element(my_array))


