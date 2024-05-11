# Following is the syntax for creating dictionary 
programming_dictionary = {
    "Bug":"An error in a program.",
    "Function": "A piece of a code that you can easily call over and over again.",
    "Loop": "The action of doing somethingover and over again.",

}

key= "Loop"
# Retriving the dictionary value using key is showin in below
print(programming_dictionary["Loop"])

# We get key error if you put wrong key thats not in the dictionary


# Adding new items to dictionary
    # programming_dictionary ["key"] = "value"
programming_dictionary["Bug"] = "It's an insects"
print(programming_dictionary["Bug"])


# Creating an empyt dictionary
empty_dict = {}

# Wipping the dictionary
# programming_dictionary ={}
# print(programming_dictionary)


# Looping through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


