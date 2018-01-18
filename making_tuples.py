def dictionary_to_Tuple(dictionary):
    new_list = []
    for key in dictionary:
        new_list.append((key,dictionary[key]))
    return new_list

my_dictionary = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

print dictionary_to_Tuple(my_dictionary)