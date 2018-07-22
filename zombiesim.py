def setValues(): #set gen 0 values
    CarrierPop = int(input ("What should the original population of Carriers be?"))
    ZombiePop = int(input ("What should the original population of Zombies be?"))
    BloaterPop = int(input ("What should the original population of Bloaters be?"))
    CarrierSur = int(input ("What should the survival rate of the Carriers be?"))
    ZombieSur = int(input ("What should the survival rate of the Zombies be?"))
    BloaterSur = int(input ("What should the survival rate of the Bloaters be?"))
    InfectRate = int(input ("What should the infection rate be?"))
    Generations = int(input ("How many generations should be simulated (between 5-25)?"))
    return CarrierPop, ZombiePop, BloaterPop, CarrierSur, ZombieSur, BloaterSur, InfectRate, Generations

def checkValues(): #check values are valid
    CarrierPop, ZombiePop, BloaterPop, CarrierSur, ZombieSur, BloaterSur, InfectRate, Generations=setValues()
    if CarrierPop < 1:
        #print ("mynamejeff1")
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

    
while True: #loop
    print ("Hello, and welcome to the zombie simulation! You have four options:")
    print (" 1: Set the Generation 0 values. \n 2: Display said values. \n 3: Run the simulation and export data to a .txt file. \n 4: Exit.")
    pick = input ("Please insert the number of your choice in numerical form.\n>") #choose on menu

    if pick == "1": #set gen 0 values
        checkValues()
