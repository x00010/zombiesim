#imports
import os.path

#global variables as i cant be bothered with passing variables
CarrierPop = 0
ZombiePop = 0
BloaterPop = 0
CarrierSur = 0
ZombieSur = 0
BloaterSur = 0
InfectRate = 0
Generations = 0

def setValues(): #set gen 0 values

    global CarrierPop #calling all global variables for editing
    global ZombiePop
    global BloaterPop
    global CarrierSur
    global ZombieSur
    global BloaterSur
    global InfectRate
    global Generations

    CarrierPop = int(input ("What should the original population of Carriers be?"))
    ZombiePop = int(input ("What should the original population of Zombies be?"))
    BloaterPop = int(input ("What should the original population of Bloaters be?"))
    CarrierSur = int(input ("What should the survival rate of the Carriers be?"))
    ZombieSur = int(input ("What should the survival rate of the Zombies be?"))
    BloaterSur = int(input ("What should the survival rate of the Bloaters be?"))
    InfectRate = int(input ("What should the infection rate be?"))
    Generations = int(input ("How many generations should be simulated (between 5-25)?"))

def checkValues(): #check values are valid
    if CarrierPop < 1:
        #print ("mynamejeff1") was used for debug purposes
        print ("Invalid value detected! Input must be redone!")
        setValues()
        
    if ZombiePop < 1:
        #print ("mynamejeff2")
        print ("Invalid value detected! Input must be redone!")
        setValues()
        
    if BloaterPop < 1:
        #print ("mynamejeff3")
        print ("Invalid value detected! Input must be redone!")
        setValues()
    
    if CarrierSur > 0:
        if CarrierSur < 1:
            pass
        
    else:
        #print ("mynamejeff4")
        print ("Invalid value detected! Input must be redone!")
        setValues()

    if ZombieSur > 0:
        if ZombieSur < 1:
            pass
        
    else:
        #print ("mynamejeff5")
        print ("Invalid value detected! Input must be redone!")
        setValues()

    if BloaterSur > 0:
        if BloaterSur < 1:
            pass
        
    else:
        #print ("mynamejeff6")
        print ("Invalid value detected! Input must be redone!")
        setValues()

    if Generations >= 5:
        if Generations <= 25:
            pass
        
    else:
        #print ("mynamejeff7")
        print ("Invalid value detected! Input must be redone!")
        setValues()

def displayValues():
    print ("\n" + str(CarrierPop) + "\n")
    print (str(ZombiePop) + "\n")
    print (str(BloaterPop) + "\n")
    print (str(CarrierSur) + "\n")
    print (str(ZombieSur) + "\n")
    print (str(BloaterSur) + "\n")
    print (str(InfectRate) + "\n")
    print (str(Generations) + "\n")

def runSim(): #oh boy, here we go!
    i = 0
    while True:
         if i > Generations:
             break
         filename = input ("Hi, what do you want the name of the output file to be?")
         if os.path.isfile(filename + ".txt") == True: #checks if file already exists
             choice = input ("This file already exists, do you want to overwrite it (y or n)?\n>")
             if choice.lower() == "y":
                 f = open(filename + ".txt","w") #opens file
                 CarrierPopFinal = CarrierPop * CarrierSur #how many carriers remain
                 ZombiePopFinal = ZombiePop * ZombieSur #how many zombies remain
                 BloaterPopFinal = BloaterPop * BloaterSur #how many bloaters remain
            
                 ZombiePopFinal = ZombiePopFinal + CarrierPopFinal
                 CarrierPopFinal = CarrierPopFinal - CarrierPopFinal #carriers change to zombies

                 CarrierPopFinal = ZombiePop * InfectRate #gives new carriers in generation

                 BloaterPopFinal = BloaterPopFinal + ZombiePopFinal
                 ZombiePopFinal = ZombiePopFinal - ZombiePopFinal #zombies change to bloaters


                 f.write("Generation" + str(i) + "\n") #gen one
                 f.write("Carrier amount = " + str(CarrierPopFinal) + "\n")
                 f.write("Zombie amount = " + str(ZombiePopFinal) + "\n")
                 f.write("Bloater amount = " + str(BloaterPopFinal) + "\n")

                 while i < Generations:
                     i = i + 1
                     CarrierPopInc = ZombiePopFinal * InfectRate #gives new carriers in generation
                     CarrierPopFinal = CarrierPopFinal + CarrierPopInc #adds extra carriers
                     CarrierPopFinal = CarrierPopFinal * CarrierSur #how many carriers remain
                     ZombiePopFinal = ZombiePopFinal * ZombieSur #how many zombies remain
                     BloaterPopFinal = BloaterPopFinal * BloaterSur #how many bloaters remain
            
                     ZombiePopFinal = ZombiePopFinal + CarrierPopFinal
                     CarrierPopFinal = CarrierPopFinal - CarrierPopFinal #carriers change to zombies

                     BloaterPopFinal = BloaterPopFinal + ZombiePopFinal
                     ZombiePopFinal = ZombiePopFinal - ZombiePopFinal #zombies change to bloaters

                     f.write("Generation" + str(i) + "\n") #gen x
                     f.write("Carrier amount = " + str(CarrierPopFinal) + "\n")
                     f.write("Zombie amount = " + str(ZombiePopFinal) + "\n")
                     f.write("Bloater amount = " + str(BloaterPopFinal) + "\n")
                     #print ("mynamejeff")
                 if i >= Generations:
                     f.close()
                     break
             if choice.lower() == "n":
                 pass
         else:
            f = open(filename + ".txt","w") #opens file
            CarrierPopFinal = ZombiePop * InfectRate #gives new carriers in generation
            CarrierPopFinal = CarrierPopFinal * CarrierSur #how many carriers remain
            ZombiePopFinal = ZombiePop * ZombieSur #how many zombies remain
            BloaterPopFinal = BloaterPop * BloaterSur #how many bloaters remain
            
            ZombiePopFinal = ZombiePopFinal + CarrierPopFinal
            CarrierPopFinal = CarrierPopFinal - CarrierPopFinal #carriers change to zombies

            BloaterPopFinal = BloaterPopFinal + ZombiePopFinal
            ZombiePopFinal = ZombiePopFinal - ZombiePopFinal #zombies change to bloaters


            f.write("Generation" + str(i) + "\n") #gen one
            f.write("Carrier amount = " + str(CarrierPopFinal) + "\n")
            f.write("Zombie amount = " + str(ZombiePopFinal) + "\n")
            f.write("Bloater amount = " + str(BloaterPopFinal) + "\n")

            while i < Generations:
                CarrierPopFinal = ZombiePopFinal * InfectRate #gives new carriers in generation
                CarrierPopFinal = CarrierPopFinal * CarrierSur #how many carriers remain
                ZombiePopFinal = ZombiePopFinal * ZombieSur #how many zombies remain
                BloaterPopFinal = BloaterPopFinal * BloaterSur #how many bloaters remain
            
                ZombiePopFinal = ZombiePopFinal + CarrierPopFinal
                CarrierPopFinal = CarrierPopFinal - CarrierPopFinal #carriers change to zombies

                BloaterPopFinal = BloaterPopFinal + ZombiePopFinal
                ZombiePopFinal = ZombiePopFinal - ZombiePopFinal #zombies change to bloaters

                f.write("Generation" + str(i) + "\n") #gen x
                f.write("Carrier amount = " + str(CarrierPopFinal) + "\n")
                f.write("Zombie amount = " + str(ZombiePopFinal) + "\n")
                f.write("Bloater amount = " + str(BloaterPopFinal) + "\n")
                i = i + 1
                f.close()

while True: #loop
    print ("Hello, and welcome to the zombie simulation! You have four options:")
    print (" 1: Set the Generation 0 values. \n 2: Display said values. \n 3: Run the simulation and export data to a .txt file. \n 4: Exit.")
    pick = input ("Please insert the number of your choice in numerical form.\n>") #choose on menu

    if pick == "1": #set gen 0 values
        setValues()
        checkValues()

    if pick == "2": #display gen 0 values:
        displayValues()

    if pick == "3": #run sim
        #here comes the hard part!
        runSim()

    if pick == "4": #close program
        break