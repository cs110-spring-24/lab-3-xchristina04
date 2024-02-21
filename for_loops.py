print("Options: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
run = int(input("Enter the problem you want to run: "))
print(f"Running problem {run}")

if run == 1:
    for num in range(1, 1001):
        print(num)
elif run == 2:
    for num in range(1, 1001, 2):
        print(num)
elif run == 3:
    for num in range(0, 1001):
        if num % 3 == 0 and num != 0:
            print(num)
elif run == 4:
    for num in range(1, 1001):
        if num % 3 == 0 or num % 5 == 0:
            print(num)
elif run == 5:
    user = int(input("Enter a number greater than 200: "))
    while True:
        if user >= 200:
            for num in range(1, user):
                if num % 11 == 0 or num % 13 == 0:
                    print(num)
            break
        else:
            user = int(input("Please enter a number greater than 200: "))
elif run == 6:
    string = input("Enter a string: ")
    for l in range(len(string)):
        print(string[l])
elif run == 7:
    string = input("Enter a string: ")
    while True:
        if len(string) >= 10:
            for l in range(0, len(string), 2):
                print(string[l])
            break
        else:
            string = input("Please enter another string: ")
elif run == 8:
    import random
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    for rolls in range(1000):
        dice = random.randint(1, 6)
        if (dice == 1):
            one += 1
        elif (dice == 2):
            two += 1
        elif (dice == 3):
            three += 1
        elif (dice == 4):
            four += 1
        elif (dice == 5):
            five += 1
        else:
            six += 1
    print(f"1 was rolled {one} times", f"2 was rolled {two} times", f"3 was rolled {three} times", f"4 was rolled {four} times", f"5 was rolled {five} times", f"6 was rolled {six} times", sep = "\n")
elif run == 9:
    num = int(input("Enter a number: "))
    if num > 1:
        for x in range(2, int(num**0.5) + 1):
            if num % x == 0:
                print(num, "is not a prime number.")
                break
        else:
            print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
else:
    for number in range(2, 1000):
        prime = 1
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                prime = 0
                break
        if prime:
            print(number)
