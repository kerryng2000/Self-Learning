#Indention for loop

pizzas = ['pepperoni', 'cheese', 'tomato']
for pizza in pizzas:
    print("I Like: " + pizza)

print("Pizza is good.")

#range(n,m): generate a series of numbers (n to m-1)
#range(n,m,s): s = numbers to skip.
#min()
#max()
#sum()
value = list(range(1,20))
print(value);

threes = [three*3 for three in range(3,30)]
print(threes)

cubed = [num**3 for num in range(1,11)]
print(cubed)

#list[0:3] for 0,1,2 elements in the list
#copying array = array2 = array1[:]
#list that is immutable is a tuple.
#tuple defined with () instead of [].

Buffet = ('a','b','c','d','e')
for dish in Buffet:
    print(dish)
#Buffet[0] = 'k' - error checking

