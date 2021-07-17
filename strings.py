# Lists can contain primative data types such as intergers, floats, booleans, & strings.
# Lists are different than strings or tuples.

# empty list
example_list = []
# list of integers
integer_list = [10, 20, 30]
# list with mixed data types
mixed_list = [22, "Text Characters", 55, "True", False]
# nested list
nested_list = ["data", [100, 22, 99], ['xyz']]

#List Methods
#append() - adds an element at the end of the list
append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list') 
print(append_example)
#insert() - adds an element at the specified index
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
#remove() - removes the first occurrence of the specified value
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)
#pop() - removes the element at the specified index
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
#clear() - removes all items from the list
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)
#index() - returns the index of the first occurrence of the specified value
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('banana'))
#count() - returns the number of occurrences of the specified value
fruits = ['apple', 'banana', 'cherry', 'banana', 'cherry']
print(fruits.count('banana'))
#sort() - sorts the list in ascending order
fruits = ['apple', 'banana', 'cherry']
fruits.sort()
print(fruits)
#reverse() - reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
#copy() - returns a copy of the list
fruits = ['apple', 'banana', 'cherry']
fruits2 = fruits.copy()
print(fruits2)

