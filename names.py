# def names(students):
#     for key in students:
#         print key["first_name"] +" "+ key["last_name"]

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name': 'John', 'last_name' : 'Rosales'},
#      {'first_name': 'Mark', 'last_name' : 'Guillen'},
#      {'first_name': 'KB', 'last_name' : 'Tonel'}
# ]

# names(students)

def names2(users):#users is the 1st key, then students and instructors is the 2nd key, then first_name and last_name become the 3rd key.
    for key in users:
        if key == "Students":
            print "Students"
            counter = 0
            for i in users[key]:#users is the key and its values are 'Students' and 'Instructors'
                counter += 1
                print counter,"-",i["first_name"] +" "+ i["last_name"],"-",len(i["first_name"])+len(i["last_name"])#i becomes a key for first_name & last_name. The value is in the [] bracket.
        elif key =="Instructors":
            print "Instructors"
            counter = 0
            for i in users[key]:
                counter += 1
                print counter,"-",i["first_name"] +" "+ i["last_name"],"-",len(i["first_name"])+len(i["last_name"])

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}

names2(users)