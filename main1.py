stop = 0

while stop != 1:
    num = int(input("How many products are you buying: "))
    if num == 1:
        break
    r = range(1, num+1)
    with open("shopping_list.txt", "w") as file:
        for i in r:
            products = input(f"Pls, enter product {i} name that you are buying:  ")
            file.write(products + "\n") 
    
    with open("shopping_list.txt", "r") as f:
        print(f.read())


    f = open("shopping_list.txt", 'r')
    print(f.read())
    
    print("To stop program, enter 1!!!")
    
    
print("Thank you to use our programm!")