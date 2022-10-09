def main():
    inputs()
    molecalculating()
    minimum()
    chopreround()
    rounding()
    multiplication()

def inputs():

    #get inputs for wheight of outputs and unknown hydrocarbon
    choinput = input("Type wheight for the unkown CHO (Use Grams): ")
    h2oinput = input("Type wheight for the unkown H2O (Use Grams): ")
    co2input = input("Type wheight for the unkown CO2 (Use Grams): ")

    #make inputs float and make then global variables
    inputs.cho = float(choinput)
    inputs.h2o = float(h2oinput)
    inputs.co2 = float(co2input)

def molecalculating():

    #define mole wheights
    carbon = 12.011
    oxygen = 15.999
    hydrogen = 1.008

    #oxygen wheight
    o2weight = inputs.h2o + inputs.co2 - inputs.cho

    #Get group moles
    co2mol = carbon + (2 * oxygen)
    h2omol = (hydrogen * 2) + oxygen
    
    #carbon and co2 oxygen moles
    carbonmol = inputs.co2 / co2mol
    co2oxygenmol = (inputs.co2 / co2mol) * 2

    #hydrogen and h2o moles
    hydrogenmol = (inputs.h2o / h2omol) / 2
    h2ooxygenmol = inputs.h2o / h2omol

    #oxygen moles
    o2mol = o2weight / oxygen

    #get all cho stuff
    finalo2 = (co2oxygenmol + h2ooxygenmol) - o2mol
    
    #make and assign values to choarray
    molecalculating.choarray = []
    molecalculating.choarray.extend([hydrogenmol, carbonmol, finalo2])

def minimum():

    #function is used to hide ugly logic
    if molecalculating.choarray[1] > molecalculating.choarray[0] and molecalculating.choarray[0] < molecalculating.choarray[2]:

        minimum.divideby = molecalculating.choarray[0]

    elif molecalculating.choarray[0] > molecalculating.choarray[1] and molecalculating.choarray[1] < molecalculating.choarray[2]:

        minimum.divideby = molecalculating.choarray[1]

    else:
        minimum.divideby = molecalculating.choarray[2]

def chopreround():
    chopreround.preroundh = molecalculating.choarray[0] / minimum.divideby
    chopreround.preroundc = molecalculating.choarray[1] / minimum.divideby
    chopreround.preroundo = molecalculating.choarray[2] / minimum.divideby

def rounding():
    
    #make array for stuff to round to
    roundingarray = []
    roundingarray.extend([0.00, 0.20, 0.25, 0.33, 0.50, 0.66, 0.75, 1.00])
    
    #Make array for multiplication
    multiplyby = []
    multiplyby.extend([1, 5, 4, 3, 2, 3, 4, 1])

    #get largest int from all vlaues
    h = int(chopreround.preroundh)
    c = int(chopreround.preroundc)
    o = int(chopreround.preroundo)
    
    #Get numbers without anything before the decimal
    lowh = chopreround.preroundh - h
    lowc = chopreround.preroundc - c
    lowo = chopreround.preroundo - o
    
    #add 1 to the one that is 0
    if lowh == 0:
        lowh += 1
    elif lowc == 0:
        lowc += 1
    else:
        lowo += 1

    #get closest rounding value
    rounding.hround = roundingarray[min(range(len(roundingarray)), key = lambda i: abs(roundingarray[i]-lowh))]
    rounding.cround = roundingarray[min(range(len(roundingarray)), key = lambda i: abs(roundingarray[i]-lowc))]
    rounding.oround = roundingarray[min(range(len(roundingarray)), key = lambda i: abs(roundingarray[i]-lowo))]

    #get values to multiply for hydrogen(h)
    timeshindex = roundingarray.index(rounding.hround)
    rounding.timesh = multiplyby[timeshindex]

    #get values to multiply for carbon(c)
    timescindex = roundingarray.index(rounding.cround)
    rounding.timesc = multiplyby[timescindex]

    #get values to multiply for oxygen(o)
    timesoindex = roundingarray.index(rounding.oround)
    rounding.timeso = multiplyby[timesoindex]

def multiplication():

    #define multiply
    multiply = rounding.timesh * rounding.timesc * rounding.timeso

    #logic for getting correct multiplication
    if rounding.timesh == rounding.timesc or rounding.timesh == rounding.timeso:
        finalmultiply = multiply / rounding.timesh

    elif rounding.timesc == rounding.timeso:
        finalmultiply = multiply / rounding.timesc

    elif rounding.timesh == rounding.timesc and rounding.timesc == rounding.timeso:
        finalmultiply = multiply / rounding.timesh / rounding.timesc
    else:
        finalmultiply = multiply

    finalc = rounding.cround * finalmultiply
    finalh = rounding.hround * finalmultiply
    finalo = rounding.oround * finalmultiply

    print("Your final hydro-carbon is: C" + str(int(finalc)) + " H" + str(int(finalh)) + " O" + str(int(finalo)))
    print("You may need to find the least common multiple")

main()