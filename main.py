import random
Computer_choice = random.choice([-1 , 0 , 1])
Your_choice = input("Enter any one of Water, Gun and Snake: ")
Mychoice = {
    "Water" : -1 ,
    "WATER" : -1 ,
    "water" : -1 ,
    "Snake" : 0 ,
    "SNAKE" : 0 ,
    "snake" : 0 ,
    "Gun" : 1 ,
    "GUN" : 1 ,
    "gun" : 1
            }

reverse_dict = {
    -1 : "Water" ,
    0 : "Snake" ,
    1 : "Gun" ,
}

you = Mychoice[Your_choice]

print(f"You chose : {reverse_dict[Mychoice[Your_choice]]}")
print(f"Computer Chose: {reverse_dict[Computer_choice]}")

if( you == Computer_choice) :
    print("Oh! It's a tie.")
else:
    if(Computer_choice == 1 and you == -1):
        print("You Won")
    elif(Computer_choice == -1  and you == 0):
        print("You Won")
    elif(Computer_choice == 0 and you == 1):
        print("You Won")
    elif(Computer_choice == 1 and you == 0):
        print("You lose")
    elif    (Computer_choice == -1 and you == 1 ):
        print("You lose")
    elif(Computer_choice == 0 and you == -1):
        print("You lose")
    else: print("Something went wrong!!!")

