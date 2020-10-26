#in/not for lists
cars = ['bmw','tesla','lexus']
if 'tesla' in cars:
    print("TSM")
if 'tesla' and 'lexus' in cars:
    print("TSM")
#elif = else if
#else block not required in elif.
aliens = ['green','yellow','red']
alien = 'red'
if alien == 'purple':
    print("What")
elif alien == 'rainbow':
    print("How")
else:
    print("Correct")
#list=[], if(List) checks if its empty
SJSU = ['San Jose']
Locations= ['Oakland','San Jose']
for location in SJSU:
    if location in Locations:
        print("TSM")
    else:
        print("Huh?")
#Spacing is better in if statements.
