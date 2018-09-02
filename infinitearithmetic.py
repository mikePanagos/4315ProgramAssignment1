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
                raise
        else:
            raise
    else:
        raise
except:
    print("infinitearithmetic \"input=<filename>;digitsPerNode=<number>\"")
    exit()

try:
    inputTxt = open(inputfile, "r")
except Exception as err:
    print(err)
    exit()

getLines(inputTxt)
# print(lines)


returnlines = list()


# goes through the list of equations looks to see it its + or * then solves it accordingly and pushes it to a new list
def recurseList(n):
    if (n == len(lines)):
        return 0
    else:
        if "+" in lines[n]:
            a, b = lines[n].split("+")
            result = (int(a)+int(b))
            returnlines.append(lines[n]+"="+str(result))
        elif "*" in lines[n]:
            a,b= lines[n].split("*")
            result =(int(a)*int(b))
            returnlines.append(lines[n]+"="+str(result))
        recurseList(n+1)



# strMath(lines[10])
recurseList(0)
# print(returnlines)
writeLines("out.txt", returnlines)
