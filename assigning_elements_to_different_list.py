#assigning elements to different lists
list1 = [4, 2, 8, 5]
list2 = [13, 67, 737, 98]

list1.append(3)
list2.append(101)

print(list1)
print(list2)


#accesing elements from a tuple
tuple1 = (1, 2, 3, 4)
print(tuple1[2])


#deleting different dictionary elements
dict1 = {
    "white": "common",
    "grey": "uncommon",
    "blue": "rare",
    "purple": "epic",
    "yellow": "legendary"
}
del dict1["blue"]
del dict1["white"]
print(dict1)



