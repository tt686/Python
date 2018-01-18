#List 1
mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [1,2,3,4,5]
string_list = ["Spiff", "Moon", "Robot"]

def identify_list_type(arr_lst):
    new_str = ""
    sum = 0

    for value in arr_lst: 
        if type(value) == int or type(value) == float:
            sum += value
        elif type(value) == str:
             new_str += value + " "
    
    if new_str and sum:
        print "The list you entered is of mixed type"
        print "String:", new_str
        print "Sum: ", sum
    elif new_str:
        print "The list you entered is of string type"
        print "String: ", new_str

    else:
        print "The list you entered is a numerical value"
        print "Sum: ", sum

identify_list_type(mixed_list)
identify_list_type(integer_list)
identify_list_type(string_list)






