stop = 0
marks = 0

while stop != 1:
    num = int(input("How many student's marks do you add: "))
    if num == 1:
        break
    r = range(1, num+1)
    with open("grades.txt", "w") as file:
        for i in r:
            name = input(f"Pls, enter student  name {i} :  ")
            file.write(name + ": ") 
            mark = int(input(f"Pls, enter student mark {i}: "))
            file.write(str(mark) + "\n") 
            marks += mark
    
    with open("grades.txt", "r") as f:
        print(f.read())
    
    average = float(marks / num)
    print(f"Avarage mark is {average}")
    print()
    
    print("To stop program, enter 1!!!")
    
    
print("Thank you to use our programm!")