'''
#print lists using for loop
the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This first kind of forloop goes through a list
for number in the_count:
    print(f"This is count {number} ")

#same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit} ")

#we alsi can go through mixed lists too
#notice we have to use {} since we dont know what's in it
for i in change:
    print(f"I got {i} ")

#we can also build lists, first start with an empty one
elements = []
#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
# append is a function that lists understand
    elements.append(i)
# now we can print them out too
for i in elements:
    print(f"Element was: {i}")
'''





'''
#while loop
i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The Numbers:")
for num in numbers:
    print(num,", ", end="")
'''


'''
from sys import exit

def gold_room():
    print("This room is full of gold. how much do you take? ")
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int (choice)
    else: 
        dead("Man, print to type a number.")

    if how_much < 50:
        print("Nice, you are not greedy, you win!")
        exit(0)
    else: 
        dead("you greedy bastard! ")

def bear_room():
    print("There is a bear here.")
    print("The bear has a jar of honey. ")
    print("The fat bear is in front of another door. ")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")
        if choice == "take honey":
            dead ("The bear looks at you then slaps your face. ")
        elif choice == "taunt bear" and not bear_moved:
                print("The bear has moved from the door. ")
                print("you can go through it now.")
                bear_moved = True
        elif choice == "taunt bear" and bear_moved:
                dead("The bear gets pissed off and chews your legs.")
        elif choice == "open door" and bear_moved:
                    gold_room()
        else: 
                    print("I got no idea what that means. ")

            
def cthulhu_room():
    print("Here you see the graet evil Cthululhu. ")
    print("He, it, whatever stares at you and you go insane. ")
    print("Do you flee for your life or eat your head? ")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else: cthulhu_room()

def dead (why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room. ")
    print("There is a door to your right and left. ")
    print("Which one do you take. ")
    choice = input("> ")

    if choice == "left":
        bear_room()
    else:
        dead("You stumble around the room until you starve. ")\

start()


'''



# doing things to lists
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. let's fix that. ")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) !=10:
    next_one = more_stuff.pop()
    print ("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now. ")

print("There we go: ", stuff)
print("Let's do some things with stuff. ")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:7]))