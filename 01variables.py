x = 5 # x is of type int
name = "John" # name is of type string
print(x)
print(name)

# List 
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
print("List: ", fruits, numbers)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result_add = list1 + list2  # result [1, 2, 3, 4, 5, 6]

list3 = [1, 2, 3]
result_mul = list3 * 3  # result [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Tuple likes List but it doesn't update
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4, 5)
print("Tuple: ", fruits, numbers)

# Set doesn't duplicate
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
print("Set: ", fruits, numbers)

# Dictionary (key: value)
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Dictionary: ", person)


