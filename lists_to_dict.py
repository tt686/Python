#Create a function that takes in two lists and creates a single dictionary.
#The first list contains keys and the second list contains the values.
#Assume the lists will be of equal length.

#Your first function will take in two lists containing some strings. Here are two example lists:

# name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
# favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

# def make_dict(list1,list2):
#     combine = zip(name,favorite_animal)
#     # print combine
#     final_dict = dict(combine)
#     print final_dict

# make_dict(name,favorite_animal)

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1,list2):
    my_dict = {}
    for i in range(0,len(list1)):
        my_dict[list1[i]]=list2[i]
    print my_dict

make_dict(name,favorite_animal)
#Hacker Challenge:
#If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.

