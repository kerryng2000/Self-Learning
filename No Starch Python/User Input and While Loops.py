
message = input("Pizza Toppings: ");

while message != 'none':
    print (message);
    message = input("Pizza Toppings: ");

num = input("Age? ");
num = int(num);
while num != 0:
    if num < 3:
        print("Free")
    elif num > 3 & num < 12:
        print("$10");
    else:
        print("$15");
    num = input("Age? ");
    num = int(num);

sandwich_orders = ['1','2','3'];
finished_sandwich = [];
while sandwich_orders:
    current_order = sandwich_orders.pop();
    finished_sandwich.append(current_order);
    print(finished_sandwich);

#while 1 == 1:
    #print("Runtime: Infinity");