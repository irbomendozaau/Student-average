total = int(input("How many students? "))
print()

for i in range(total):
    print("Student ", i + 1)
    
    name = input("Enter your name: ")
    
    act1 = int(input("Activity 1: "))
    act2 = int(input("Activity 2: "))
    act3 = int(input("Activity 3: "))
    
    totalscore = act1 + act2 + act3
    average = totalscore / 3
    
    print("Average: ", average)
    
    if average >= 90:
        print("Status: Excellent")
    elif average >= 80:
        print("Status: Very Good")
    elif average >= 75:
        print("Status: Passed")
    else:
        print("Status: Failed")

