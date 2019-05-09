
#
#   ROYCE GUERRA
#   PROJECT 8
#

import os 

fileSource     = open('AlsAutoInv.txt','r')
tempSourceCopy = open('tempTxt.txt','w')

def main():
    totalLines  = 0
    writtenLine = 0
    for line in fileSource:
        totalLines += 1
    # fix SPECIFIC 
        if 'PART' in line.upper():
            goodType, goodPart, goodDesc, goodQty,\
            goodLoc, goodCost, goodPrice, goodMake,\
            goodModel, yearStart, yearEnd = fixPartSpecific(line.split('*'))
            line = '*{}*{}*{}*{}*{}*{}*{}*{}*{}*{}*{}\n'.format(goodType, goodPart, goodDesc, goodQty,\
            goodLoc, goodCost, goodPrice, goodMake,\
            goodModel, yearStart, yearEnd)
            
            tempSourceCopy.write(line)
            writtenLine += 1
                
    # fix COMMON 
        if 'ACC' in line.upper():
            goodType, goodPart, goodDesc, goodQty,\
            goodLoc, goodCost, goodPrice = fixCommon(line.split('*'))
            line = '*{}*{}*{}*{}*{}*{}*{}*\n'.format(goodType, goodPart, goodDesc, goodQty,\
            goodLoc, goodCost, goodPrice)
            
            tempSourceCopy.write(line)
            writtenLine +=1
            
    fileSource.close()
    tempSourceCopy.close()
    print('Lines Written: ',writtenLine)
    print('Total Read:    ',totalLines)
    os.rename('AlsAutoInv.txt','AlsAutoInv_Old.txt')
    os.rename('tempTxt.txt','AlsAutoInv.txt')
    
# call worker bee functions
def fixCommon(inputString):
    goodType  = fixType(inputString[1])
    goodPart  = fixPart(inputString[2])
    goodDesc  = fixDesc(inputString[2]) 
    goodQty   = fixQty(inputString[3])
    goodLoc   = fixLoc(inputString[4])
    goodCost  = fixCost(inputString[5])
    goodPrice = fixPrice(inputString[6])
    return goodType, goodPart, goodDesc, goodQty,\
           goodLoc, goodCost, goodPrice
    

def fixPartSpecific(inputString):
    goodType  = fixType(inputString[1])
    goodPart  = fixPart(inputString[2])
    goodDesc  = fixDesc(inputString[2])
    goodQty   = fixQty(inputString[3])
    goodLoc   = fixLoc(inputString[4])
    goodCost  = fixCost(inputString[5])
    goodPrice = fixPrice(inputString[6])
    goodMake  = fixMake(inputString[7])
    goodModel = fixModel(inputString[8])
    yearStart = fixYearS(inputString[9])
    yearEnd   = fixYearE(inputString[9])
    return goodType, goodPart, goodDesc, goodQty,\
           goodLoc, goodCost, goodPrice, goodMake,\
           goodModel, yearStart, yearEnd
    
# worker bee functions
def fixType(badType):
    goodType = badType.capitalize()
    goodType = goodType.strip()
    return goodType

def fixPart(badPart):
    goodPart = badPart.strip()
    goodPart = goodPart[0:8]
    goodPart = goodPart.replace('O','0')
    return goodPart

def fixDesc(badDesc):
    goodDesc = badDesc[8:]
    goodDesc = goodDesc.strip()
    result   = ''
    for char in goodDesc:
        if (char.isupper()):
            result = result + ''
        result = result + char
    return result

def fixQty(badQty):
    goodQty   = int(badQty)
    return goodQty

def fixLoc(badLoc):
    goodLoc   = badLoc.strip().replace(' ','')
    return goodLoc

def fixCost(badCost):
    goodCost  = float(badCost.replace('$','').replace(',',''))
    return goodCost

def fixPrice(badPrice):
    goodPrice = float(badPrice.replace('$','').replace(',',''))
    return goodPrice
'''
SPECIFIC
'''
def fixMake(badMake):
    goodMake  = badMake.strip()
    return goodMake

def fixModel(badModel):
    goodModel = badModel.strip()
    return goodModel

def fixYearS(badYear):
    yearStart = int(badYear[:4])
    return yearStart

def fixYearE(badYear):
    yearEnd   = int(badYear[5:])
    return yearEnd

main()

'''
TESTING: 
- Tested using a previous assignments input to ensure i was sending
the right information to and from functions. Tested my code at the beggining
by running short lines of code to ensure i was creating the proper .txt files
and creating one line of code to start.


PROJECT SUMMARY:
Where did you get stuck, and how did you get unstuck?
- I mostly got hungup on how to use the returned information from
the small worker bee functions. implementing them took some time to
figure out, its something i have been working on getting stronger
with. 

How did you test your program?
- I tested mostly by running one line of code at the start and
making sure i was able to create my .txt files. 



'''













