#Create a dictionary
dictionary = {}


"""Add elements to the dictionary"""

#"""KV Dodan as name and 26 as age
dictionary["Dodan"] = 26

#"""KV Andra as name and a list of 2 values
dictionary["Andra"] = ["Laminare", 24]

# Prices as Key and Value = A list of a dictionary and a few values
dictionary["Prices"] = [
    {
        "Potato" : 25,
        "Tomato" : 22
     },
     25, 26, "Blabla"
]

print(dictionary)


"""Removing elements from dictionary"""

#We can use key word "del" or .pop() function to remove a element from dictionary
del dictionary["Dodan"]
#dictionary.pop("Dodan")
print(dictionary)


"""Iteration in a dictionary"""

for key, value in dictionary.items():
    print(key, ':', value)

#OR

for key in dictionary:
    print(key, ':', dictionary[key])


"""Appending a dictionary to a list"""

list_for_dict = []
list_for_dict.append(dictionary)
print(list_for_dict)
