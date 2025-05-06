# 1 lists
# create a list, append '6', delete 1st element

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.pop(1)
print(numbers)

################################################################################################################################

# 2 tuples
# create a tuple, try to rename an element in tuple, error because immutable
my_tuple = ("apple", "banana", "cherry", "grape")
print(my_tuple[1])
#my_tuple[1] = "blueberry"  # UNCOMMENT TO RUN and see error 

################################################################################################################################

# 3 dictionary
# create dictionary with 3 key value pairs, add another, print updated
my_dict = {
    "name": "Bulma", "age": 33, "city": "West City"   
}
my_dict["occupation"] = "capsule corp"
print(my_dict)




