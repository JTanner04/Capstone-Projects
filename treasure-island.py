print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_choose = input("Would you like to go left or right? ").lower()

if first_choose == "left":
    print("Suprised you chose the right path!")
    second_choose = input("There is a boat, would you like to ride in it or swim? ").lower()
    if second_choose == "boat":
        print("Correct you are still alive that is so, so, so suprising!")
        thrid_chose = input("You now arrive at some doors. Your options are a blue, red, green, yellow door: ")
        if thrid_chose == "blue":
            print("Wow you found the treasure, and you are now the king of the pirates")
        elif thrid_chose == "red":
            new_opition = input("You have one more chances pick a side. Right or Left: ").lower()
            if new_opition == "right":
                print("You have multiple treasures that made you a GOD!")
            else:
                print("You died!")
        else:
            print("Wow you came so close, but you are dead now!")
    else:
        print("You came far enough, but your dead now!")
else:
    print("You fell into the pits of hell!")



