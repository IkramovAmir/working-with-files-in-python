# Task 1

stop = 0

while stop != 1:
    name = input("Pls, enter your name: ")
    if name == "1":
        break
    number = input("Enter phone number. For example: +998912982933: ") 
    file = open("contacts.txt", 'a')
    file.write("\n")
    file.write(name)
    file.write(": ")
    file.write(number)
    file.close()

    f = open("contacts.txt", 'r')
    print(f.read())
    
    print("To stop program, enter 1!!!")
    
    
print("Thank you to use our programm!")