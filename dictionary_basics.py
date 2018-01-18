def about(my_dict):
    for key in my_dict:
        # print "My",key, "is", my_dict[key]
        print "My {} is {}".format(key,my_dict[key])

my_dict = {"name": "Tri", "age": 33, "country of birth": "USA", "favorite language": "Python Baby!"}

about(my_dict)

def about(my_dict):
    for key in my_dict:
        print "My",key, "is", my_dict[key]
        #or
        print "Mty {} is {}".format(key,my_dict[key])
my_dict = {"name": "Tri", "age": 33, "country of birth": "USA", "favorite languate": "Python"}

about(my_dict)
