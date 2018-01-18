word_list = ['hello','world','my','name','is','Anna']
def Find_Characters(lst, char):
    new_str = []
    for i in range (0,len(lst)):

        if lst[i].find(char) !=-1:
            new_str.append(lst[i])

    print new_str
Find_Characters(word_list, 'o')



