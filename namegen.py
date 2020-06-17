#This program generates a series of random names with a basic structure, of random or predetermined length

import random
from colorama import Fore

cons = ["b", "c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
vows = ["a","e","i","o","u","y"]
name=[]
names=[]

def banner():
    print(Fore.GREEN+"   _  __             "+Fore.WHITE+"  _____           ")
    print(Fore.GREEN+"  / |/ /__ ___ _  ___"+Fore.WHITE+" / ___/__ ___     ")
    print(Fore.GREEN+" /    / _ `/  ' \/ -_)"+Fore.WHITE+" (_ / -_) _ \    ")
    print(Fore.GREEN+"/_/|_/\_,_/_/_/_/\__/"+Fore.WHITE+"\___/\__/_//_/    ")
    print("                           by"+Fore.GREEN+" Deipy        ")
    print("")

def namegen(length, number):
    if(length!= 99):
        for i in range(0, number):
            #create empty array with proper length
            for a in range(0, length):
                name.insert(a, "")
            #fill in the array
            for b in range(0, length):
                name.append(cons[random.randint(1, len(cons)-1)])
                name.append(vows[random.randint(0, len(vows)-1)])
            n = ""
            #convert name array to string and get rid of old name
            for letter in name:
                n+=letter
            name.clear()
            #add new name to names array
            names.append(n)
    elif length == 99:
        for i in range(0, number):
            no = random.randint(mil, mal)
            #create empty array with proper length
            for a in range(0, no):
                name.insert(a, "")
            #fill in the array
            for b in range(0, no):
                name.append(cons[random.randint(1, len(cons)-1)])
                name.append(vows[random.randint(0, len(vows)-1)])
            n = ""
            #convert name array to string and get rid of old name
            for letter in name:
                n+=letter
            name.clear()
            #add new name to names array
            names.append(n)

banner()

#setting up
print(Fore.GREEN+"[?]"+Fore.WHITE+"How many sylables ? (99 for random) :")
sy = int(input())
if sy == 99:
    print(Fore.GREEN + "[?]" + Fore.WHITE + "Min length ? (sylables) :")
    mil = int(input())
    print(Fore.GREEN + "[?]" + Fore.WHITE + "Max length ? (sylables) :")
    mal = int(input())
print(Fore.GREEN+"[?]"+Fore.WHITE+"How many names ? : ")
nb = int(input())

# generate a number of names (nb) of length (sy)
print(Fore.GREEN+"[!] generating...")
namegen(sy, nb)

# print the names to console with two different format depending on length (random or not)
print(Fore.WHITE+"")
index=0
if sy != 99:
    for word in names :
            print(word+ "  |  ", end="")
            index+=1
            if(index == 3):
                print("")
                index=0
else:
    for word in names :
        print(word)
