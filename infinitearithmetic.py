from file_maker import *
import sys

inputfile = ""
digitspernode = 0
try:
    if len(sys.argv)>1:
        inputs = sys.argv[1].replace(";"," ").split()
        if len(inputs) == 2:
            (arg1, val1) = (inputs[0].split("=")[0].strip(), inputs[0].split("=")[1].strip())
            (arg2, val2) = (inputs[1].split("=")[0].strip(), int(inputs[1].split("=")[1].strip()))
            if arg1.lower() == "input" and arg2.lower() == "digitspernode":
                inputfile = val1
                digitspernode = val2
            else:
                raise Exception()
        else:
            raise Exception()
    else:
        raise Exception()
except Exception as err:
    print("python3 infinitearithmetic \"input=<filename>;digitsPerNode=<number>\"")
    exit()

try:
    inputTxt = open(inputfile, "r")
except Exception as err:
    print(err)
    exit()

#getLines(inputTxt)
# print(lines)


# returnlines = list()






def mathAdd(list, list1, list2, carry, index):
    # print("carry is ",carry)
    if(len(list1) > index and len(list2) > index):
        adding = int(list1[index])+int(list2[index])+int(carry)
    elif(len(list1) > index):
        adding = int(list1[index])+int(carry)
    elif(len(list2) > index):
        adding = int(list2[index])+int(carry)
    else:
        return list

    add = str(adding)
    # print(add)
    if(add == "0"):
        add = "0000"

    # check if the 2 segments added together is bigger then the 4 digit segment allowed if so add the last digit to carry
    if(len(add) > digitspernode):
        carry = int(add[:1])
        # print( "carry is =",carry)
        list.append(add[1:])
        # print ("the list is",list)
        if (index == len(list1)-1):
            if(carry):
                list.append(str(carry))

            return list
        else:
          return mathAdd(list, list1, list2, carry, index+1)
    else:
        list.append(add)

        carry = 0

        # print("carry is", carry)
        return mathAdd(list, list1, list2, carry, index+1)


# takes the 4 digit segments and combinds them again
def assemble(index, list):
    # print(list)
    # print ("index is ",index)
    # print(" val is ",final[index])
    if (index == len(list)-1):
        return list[index]
    return assemble(index+1, list)+list[index]


# takes a string and breaks it into 4 digit segments in reversed order
def formlists(list, num):
    if(len(num) < digitspernode):
        if(len(num) > 0):
            list.append(num)
        return list
    else:
        list.append(num[-digitspernode:])
        return formlists(list, num[:-digitspernode])


def addingZeros(index, zeroes):

    if(index == 0):
        return zeroes
    else:
        zeroes += "0"
        return addingZeros(index-1, zeroes)

    # print(assemble(0))


def mathMult(num1, num2, index, final):
    if(len(num2) > 0):
        # print(num2[-1:])
        zeros = addingZeros(index, "")
        add = str(int(num1)*int(num2[-1:]))+zeros

        if(int(add) == 0):
            return mathMult(num1, num2[:-1], index+1, final)
        else:
            final.append(add)
            return mathMult(num1, num2[:-1], index+1, final)
        # print(num2[:-1])
    else:
        # print(final)
        return final


def addAll(numberList):
    if(len(numberList)>1):
        add=int(numberList[0])+int(numberList[1])
        numberList.remove(numberList[1])
        numberList[0]=str(add)
        return addAll(numberList)
    else:

        return numberList



# goes through the list of equations looks to see it its + or * then solves it accordingly and pushes it to a new list
def recurseList(n,returnlines, lines):
    if (n == len(lines)):
        return returnlines
    else:
        if "+" in lines[n]:
            a, b = lines[n].split("+")
            if(a =="0" ):
                result=b
            elif(b=="0"):
                result=a
            else:
                result =assemble(0,mathAdd(list(),formlists(list(), a), formlists(list(), b), 0, 0))
            # result = (int(a)+int(b))
            returnlines.append(lines[n]+"="+str(result))

        elif "*" in lines[n]:
            a,b= lines[n].split("*")
            if(a=="0" or b=="0"):
                result="0"
            else:
                result = (addAll(mathMult(a,b,0,list())))
            returnlines.append(lines[n]+"="+str(result[0]))
        print (returnlines[n])
    return recurseList(n+1,returnlines, lines)

# strMath(lines[10])

# print(returnlines)
writeLines("out.txt",recurseList(0,list(), getLines(inputTxt, list())))
