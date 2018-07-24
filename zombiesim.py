#imports
import os.path

#global variables as i cant be bothered with passing variables
#CarrierPop = 0
#ZombiePop = 0
#BloaterPop = 0
#CarrierSur = 0
#ZombieSur = 0
#BloaterSur = 0
#InfectRate = 0
#Generations = 0
i = 0

def checkValues(message, lowrange, highrange):
    while True:
        value = input (message + "\n>")
        iValue = float(value)

        if highrange == -1:
            if iValue > lowrange:
                return value
                break

        if iValue <= highrange:
            if iValue >= lowrange:
                return value
                break

def setValues(): #set gen 0 values

    #CarrierPop = int(input ("What should the original population of Carriers be?"))
    CarrierPop = checkValues("What should the original population of Carriers be?", 0, -1)

    #ZombiePop = int(input ("What should the original population of Zombies be?"))
    ZombiePop = checkValues("What should the original population of Zombies be?", 0, -1)

    #BloaterPop = int(input ("What should the original population of Bloaters be?"))
    BloaterPop = checkValues("What should the original population of Bloaters be?", 0, -1)

    #CarrierSur = int(input ("What should the survival rate of the Carriers be?"))
    CarrierSur = checkValues("What should the survival rate of the Carriers be?", 0, 1)

    #ZombieSur = int(input ("What should the survival rate of the Zombies be?"))
    ZombieSur = checkValues("What should the survival rate of the Zombies be?", 0, 1)

    #BloaterSur = int(input ("What should the survival rate of the Bloaters be?"))
    BloaterSur = checkValues("What should the survival rate of the Bloaters be?", 0, 1)

    #InfectRate = int(input ("What should the infection rate be?"))
    InfectRate = checkValues("What should the infection rate be?", 0, -1)

    #Generations = int(input ("How many generations should be simulated (between 5-25)?"))
    Generations = checkValues("How many generations should be simulated (between 5 and 25)?", 5, 25)

    array = [CarrierPop, ZombiePop, BloaterPop, CarrierSur, ZombieSur, BloaterSur, InfectRate, Generations]
    return array

def displayValues(array):
    print ("\n" + array[0] + "\n")
    print (array[1] + "\n")
    print (array[2] + "\n")
    print (array[3] + "\n")
    print (array[4] + "\n")
    print (array[5] + "\n")
    print (array[6] + "\n")
    print (array[7] + "\n")

def simArray(array, f, A):
    global i
    while i < int(array[7]):
        i = i + 1
        if i == 1:
            CarrierPopInc = int(array[1]) * int(array[6]) #gives new carriers in generation
            CarrierPopFinal = int(array[0]) + CarrierPopInc #adds extra carriers
            CarrierPopFinal = CarrierPopFinal * int(array[3]) #how many carriers remain
            ZombiePopFinal = int(array[1]) * int(array[4]) #how many zombies remain
            BloaterPopFinal = int(array[2]) * int(array[5]) #how many bloaters remain
            
            ZombiePopFinal = ZombiePopFinal + CarrierPopFinal
            CarrierPopFinal = CarrierPopFinal - CarrierPopFinal #carriers change to zombies

            BloaterPopFinal = BloaterPopFinal + ZombiePopFinal
            ZombiePopFinal = ZombiePopFinal - ZombiePopFinal #zombies change to bloaters

            Total = ZombiePopFinal + CarrierPopFinal + BloaterPopFinal

            A.insert(i, [CarrierPopFinal,ZombiePopFinal,BloaterPopFinal,Total])
        else:
            CarrierPopInc = ZombiePopFinal * int(array[6]) #gives new carriers in generation
            CarrierPopFinal = CarrierPopFinal + CarrierPopInc #adds extra carriers
            CarrierPopFinal = CarrierPopFinal * int(array[3]) #how many carriers remain
            ZombiePopFinal = ZombiePopFinal * int(array[4]) #how many zombies remain
            BloaterPopFinal = BloaterPopFinal * int(array[5]) #how many bloaters remain
            
            ZombiePopFinal = ZombiePopFinal + CarrierPopFinal
            CarrierPopFinal = CarrierPopFinal - CarrierPopFinal #carriers change to zombies

            BloaterPopFinal = BloaterPopFinal + ZombiePopFinal
            ZombiePopFinal = ZombiePopFinal - ZombiePopFinal #zombies change to bloaters
        
            Total = ZombiePopFinal + CarrierPopFinal + BloaterPopFinal

            A.insert(i, [CarrierPopFinal,ZombiePopFinal,BloaterPopFinal,Total])
    else:
        f.write(str(A))
        f.close()

def runSim(array): #oh boy, here we go!
    while True:
         filename = input ("Hi, what do you want the name of the output file to be?\n>")
         if os.path.isfile(filename + ".txt") == True: #checks if file already exists
             choice = input ("This file already exists, do you want to overwrite it (y or n)?\n>")
             if choice.lower() == "y":
                 f = open(filename + ".txt","w") #opens file

                 Total = int(array[0]) + int(array[1]) + int(array[2])
                 A = [[array[0],array[1],array[2],Total]]
                 #A.insert(0, [array[1],arrau),str(BloaterPop),str(Total)])
                 simArray(array, f, A)
                 #print ("mynamejeff")
                 break
             if choice.lower() == "n":
                 pass
         else:
             f = open(filename + ".txt","w") #opens file

             Total = int(array[0]) + int(array[1]) + int(array[2])

             A = [[array[0],array[1],array[2],Total]]
            #A.insert(0, [array[1],arrau),str(BloaterPop),str(Total)])
             simArray(array, f, A)
            #print ("mynamejeff")
             break



while True: #loop
    print ("Hello, and welcome to the zombie simulation! You have four options:")
    print (" 1: Set the Generation 0 values. \n 2: Display said values. \n 3: Run the simulation and export data to a .txt file. \n 4: Exit.")
    pick = input ("Please insert the number of your choice in numerical form.\n>") #choose on menu

    if pick == "1": #set gen 0 values
        array = setValues()

    if pick == "2": #display gen 0 values
        displayValues(array)

    if pick == "3": #run sim
        #here comes the hard part!
        runSim(array)

    if pick == "4": #close program
        break