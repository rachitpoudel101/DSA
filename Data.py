""" 1. Using Lists as a basic data structure"""
# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1

# Adding elements
my_list.append(6)  # Adds 6 to the end
my_list.insert(2, 10)  # Inserts 10 at index 2

# Removing elements
my_list.remove(3)  # Removes the first occurrence of 3
popped_element = my_list.pop()  # Removes and returns the last element
print("Popped Element:", popped_element)
print("Modified List:", my_list)

"""2. Using a List as a Stack"""

stack = []       # An empty list
stack.append(1)   # Stack: [1]
stack.append(2)   # Stack: [1, 2]
popped_element = stack.pop()  # Removes and returns the last element (LIFO), which is 2
print("Popped Element from Stack:", popped_element)
print("Final Stack:", stack)

"""3. Using Dictionary"""

# Creating a dictionary
my_dict = {'key1': 'value1', 'key2': 'value2'}

# Accessing values
print("Value for 'key1':", my_dict['key1'])  # Output: 'value1'

# Modifying values
my_dict['key1'] = 'new_value'
print("Modified Dictionary:", my_dict) 


# intersection sort 

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array.pop(i)
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            insert_index = j
    my_array.insert(insert_index, current_value)

print("Sorted array:", my_array)
