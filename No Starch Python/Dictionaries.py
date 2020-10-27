#Dictionary, Key:Value pairs wrapped in {}
#str(int) converts to string value
#dictionary[tsm] = ___ = {tsm:___}
#no order in dictionary.
#del dictionary[tsm] to remove items from dictionary

Person = {'first_name' : 'Tom', 'last_name' : 'Sawyer', 'age' : 15, 'city' : 'Oakland'}
print(Person['first_name']);
print(Person['last_name']);
print(str(Person['age']));
print(Person['city']);

#.items() for dictionary for loop
#.keys() for key
#sorted() for sorting dictionaries
#.values() for values
for key,value in Person.items():
    print("Key: " + key)
    print("Value: " + str(value))

Users = {'Bob' : {'first_name' : 'Bob'}}
for user, user_info in Users.items():
    print(user + "" + user_info['first_name'])