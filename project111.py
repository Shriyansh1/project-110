import random

response = "Y"

while response == "Y":

    no = random.randint(1,6)

    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  1  ]")
        print("[     ]")
        print("[-----]")

    if no == 2:
        print("[-----]")
        print("[     ]")
        print("[  1+ ]")
        print("[  1  ]")
        print("[-----]")

    if no == 3:
        print("[-----]")
        print("[  1+ ]")
        print("[  1+ ]")
        print("[  1  ]")
        print("[-----]")
        
    if no == 4:
        print("[-----]")
        print("[ 1+1 ]")
        print("[ 1+1 ]")
        print("[     ]")
        print("[-----]")

    if no == 5:
        print("[-----]")
        print("[ 1+1 ]")
        print("[  2+ ]")
        print("[  1  ]")
        print("[-----]")

    if no == 6:
        print("[-----]")
        print("[  2+ ]")
        print("[  2+ ]")
        print("[ 1+1 ]")
        print("[-----]")

    response = input("Y to roll again in capital")
    print("\n")
