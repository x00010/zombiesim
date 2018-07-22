def setValues():
    CarrierPop = int(input ("What should the original population of Carriers be?"))
    ZombiePop = int(input ("What should the original population of Zombies be?"))
    BloaterPop = int(input ("What should the original population of Bloaters be?"))
    CarrierSur = int(input ("What should the survival rate of the Carriers be?"))
    ZombieSur = int(input ("What should the survival rate of the Zombies be?"))
    BloaterSur = int(input ("What should the survival arate of the Bloaters be?"))
    

while True: #loop
    print ("Hello, and welcome to the zombie simulation! You have three options:")
    print (" 1: Set the Generation 0 values. \n 2: Display said values. \n 3: Run the simulation. \n 4: Export data to a .txt file. \n 5: Exit.")
    pick = input ("Please insert the number of your choice in numerical form.\n>") #choose on menu

    if pick == "1": #set gen 0 values
        setValues():
