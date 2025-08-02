import os
import time

# this func draws the gear num like a 7 seg 
def display_gear (gear_num):
    # map for digits 0-8 (5x4)
    d={
        0:["####",
           "#  #",
           "#  #",
           "#  #",
           "####"],

        1:["   #",
           "   #",
           "   #",
           "   #"],

        2:["####",
           "   #",
           "####",
           "#   ",
           "####"],

        3:["####",
           "   #",
           "####",
           "   #",
           "####"],

        4:["#  #",
           "#  #",
           "####",
           "   #",
           "   #"],

        5:["####",
           "#   ",
           "####",
           "   #",
           "####"],

        6:["####",
           "#   ",
           "####",
           "#  #",
           "####"],

        7:["####",
           "   #",
           "   #",
           "   #"],

        8:["####",
           "#  #",
           "####",
           "#  #",
           "####"]                        
    }
    #check if the gear exist in the digits
    if gear_num in d:
        for i in d[gear_num]:
            print(i)
    else:
        print("bro, that gear doesn't exist")

#bonus vibes
def animate_shift(from_gear, to_gear):

    #show the current gear first

    os.system('cls' if os.name=='nt' else 'clear')
    print(f"shifting... gear :{from_gear}")
    display_gear(from_gear)
    time.sleep(1) #stop 1s

    #clear the screen

    os.system('cls' if os.name=='nt' else 'clear')

    #and here is ,new gear is in

    print(f"gear :{to_gear}")
    display_gear(to_gear)

#MAIN

while True:
    inP=input("Enter gear 0-8 or 'q' to quit :")

    #IF THE USER WANTS TO BAIL OUT

    if inP.lower()=='q':
        print("Engine off\n Catch you later <3")
        break

    #HANDLE BAD INPUTS

    if not inP.isdigit():
        print("YO ,type a number between 0 and 8 only")
        continue

    gear=int(inP)

    if gear<0 or gear>8:
        print("Nah bro ,gear go from 0 to 8 only")
        continue

    #SHOW THE GEAR

    os.system('cls' if os.name=='nt' else 'clear')
    print(f"Gear :{gear}")
    display_gear(gear)

    #ASK IF WE WANNA SHIFT GEARS

    change=input("Wanna shift to another gear?? (yup/nop) : ")
    
    if change.lower()=='yup':
        newG=input("Enter new gear 0-8 :")
        if newG.isdigit() and 0<= int(newG) <=8:
            animate_shift(gear ,int(newG))

        else:
            print("Bruh ,that's not a valid gear")




