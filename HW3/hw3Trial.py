import sys


try:
    if len(sys.argv)>1:
        inputs = sys.argv[1].replace(";"," ").split()
        if len(inputs) == 1:
             inputfile =inputs[0]
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



def getLines(f, lst):
    line = f.readline()
    if line == "":
        f.close()
        return lst
    else:
        if line[-1] == '\n':
            line = line[:-1]
        lst.append(line)
        return getLines(f, lst)

def is_number(s): 
    for i in s:
        try:
            int(i)

        except ValueError:
            return -1
    return 1

def check(lst):
    num=0
    if(is_number(lst)==1):
        for i in lst:
            num+=int(i)
        print(num)
    else:
        print("nope")

def checkM(lst):
    num=1
    if(is_number(lst)==1):
        for i in lst:
            num=num*int(i)
        print(num)
    else:
        print("nope")

def add(a,b):
    return a+b
def multiply(a,b):
    return a*b

def findAnswer(line):
    
    return 7




def eval(list):
    for i in list:
        print (i)
        i="print("+i+")"
        exec(i)





eval(getLines(inputTxt, list()))