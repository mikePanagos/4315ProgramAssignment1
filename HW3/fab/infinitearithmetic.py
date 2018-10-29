import sys
from checkCorrectness import checkIfCorrect
import functools

def checkArgs(args, vals):
    """
    Precondition: args is a 2-tuple of strings and vals is a 2-tuple of strings
    Postcondition: returns 2-tuple of strings
    """
    if args[0].lower() == "input" and args[1].lower() == "digitspernode" and vals[1] > 0:
        return (vals[0], vals[1])
    raise Exception()

def valuesFromTTY(argv):
    """
    Precondition: Vector of strings from command line
    Postcondition: returns 2-tuple of strings
    """

    try:
        if len(sys.argv)>1:
            inputs = sys.argv[1].replace(";"," ").split()
            if len(inputs) == 2:
                (arg1, val1) = (inputs[0].split("=")[0].strip(), inputs[0].split("=")[1].strip())
                (arg2, val2) = (inputs[1].split("=")[0].strip(), int(inputs[1].split("=")[1].strip()))

                values = checkArgs((arg1, arg2), (val1, val2))
            else:
                raise Exception()
        else:
            raise Exception()
    except Exception as err:
        print("python3 infinitearithmetic \"input=<filename>;digitsPerNode=<number>\"")
        exit()
    return values

def textFileStream(inputfile):
    """
    Precondition: inputfile is a string name of file
    Postcondition: returns an object of type file
    """
    try:
        inputTxt = open(inputfile, "r").read()
        inputTxt +="<EOF>"
    except Exception as err:
        print(err)
        exit()
    return inputTxt

def getLines(f, lst):
    """
    Precondition: f is the file stream and lst is a list of strings
    Postcondition: returns a list of strings representing lines in the file
    """
    line = f.readline()
    if line == "":
        f.close()
        return lst
    else:
        if line[-1] == '\n':
            arr = appendList(lst, line[:-1])
        else:
            arr = appendList(lst, line)
        return getLines(f, arr)

def getLinesFP(file):
    with open(file) as f:
        return [x.strip() for x in f.readlines() if x != ""]
    return []
    

def writeLines(name, lst):
    outf = open(name, "w")
    outf.write("\n".join(lst))


def zerofy(add, list1, list2, index, digitspernode):
    """
    Precondition: add is a string, list1 and list2 are a list of strings that make up the nodes, 
        index and digitspernode are integers
    Postcondition: returns add that will be a string with appended zeroes.
    """
    if add == "0":
        return "0" * digitspernode
    elif len(add) < digitspernode and not((index >= len(list1)) and (index >= len(list2))):
        return ("0" * (digitspernode - len(add))) + add
    return add

def appendList(arr, elem):
    """
    Precondition: arr is a list of strings, and elem is a string
    Postcondition: returns arr a list of strings with the string element elem appended to it
    """
    newArr = arr
    newArr.append(elem)
    return newArr

def removeFromList(arr, elem):
    """
    Precondition: arr is a list of strings, and elem is a string
    Postcondition: returns arr a list of strings with the string element elem removed from it
    """
    newArr = arr
    return newArr.remove(elem)

# addeds digit segments together 
def mathAdd(list, list1, list2, carry, index, digitspernode):
    """
    Precondition: list, list1 and list2 are a list of strings that make up the nodes of digits, 
        carry, index and digitspernode are integers
    Postcondition: returns list, a list of strings with an appanded string element for every call
    """
    if(len(list1) > index and len(list2) > index):
        adding = str(int(list1[index])+int(list2[index])+int(carry))
    elif(len(list1) > index):
        adding = str(int(list1[index])+int(carry))
    elif(len(list2) > index):
        adding = str(int(list2[index])+int(carry))
    else:
        return list

    add = zerofy(adding, list1, list2, index, digitspernode)

    # check if the 2 segments added together is bigger then the 4 digit segment allowed if so add the last digit to carry
    if(len(add) > digitspernode):
        carry = int(add[:1])
        arr = appendList(list, add[1:])
        if (index == len(list1)-1):
            if(carry):
                return appendList(list, str(carry))
            return list
        else:
            return mathAdd(list, list1, list2, carry, index+1, digitspernode)
    else:
        arr = appendList(list, add)
        carry = 0
        return mathAdd(arr, list1, list2, carry, index+1, digitspernode)


# takes the  digit segments and combinds them again
def assemble(index, list):
    """
    Precondition: index is an integer that'll iterate and list is a list of strings that represent nodes of digits
    Postcondition: returns a concatenated string of all the nodes
    """
    if (index == len(list)-1):
        return list[index]
    return assemble(index+1, list) + list[index]


# takes a string and breaks it into 4 digit segments in reversed order
def formlists(list, num, digitspernode):
    """
    Precondition: list is a list of strings, num is an integer, and digitspernode is an integer
    Postcondition: returns a list of strings
    """
    if(len(num) < digitspernode):
        if(len(num) > 0):
            return appendList(list, num)
        return list
    else:
        return formlists(appendList(list, num[-digitspernode:]), num[:-digitspernode], digitspernode)

# does the multiplication digit by digit 
def mathMult(num1, num2, index, final):
    """
    Precondition: num1 and num2 are numerical strings, index is an integer that iterates, and final is a list of strings
    Postcondition: returns a list of strings
    """
    if(len(num2) > 0):
        zeros="0"*index
        add = str(int(num1)*int(num2[-1:]))+zeros
        if(int(add) == 0):
            return mathMult(num1, num2[:-1], index+1, final)
        else:
            return mathMult(num1, num2[:-1], index+1, appendList(final, add))
    else:
        return final

# adds all numbers for multiplication 
def addAll(numberList):
    """
    Precondition: numberList is a list of numerical strings
    Postcondition: returns a reduced list of strings until one single string in the list
    """
    if(len(numberList) > 1):
        add=int(numberList[0])+int(numberList[1])
        numberList.remove(numberList[1])
        numberList[0]=str(add)
        return addAll(numberList)
    else:
        return numberList[0]

def evaluate(expression, digitspernode):
    if "+" in expression:
        a, b = expression.split("+")
        if(not a.isdigit() or not b.isdigit()):
            result="ERROR: improper operation "
        elif(int(a)==0):
            result=b
        elif(int(b)==0):
            result=a
        elif(not a or not b):
            result="ERROR: improper operation "
        
        else:
            # formlist breaks the number int segments then those are passed into mathAdd which address the segments and # 
            # then is assembled back into one number
            try:
                result = assemble(0, mathAdd(list(), formlists(list(), a, digitspernode), formlists(list(), b, digitspernode), 0, 0, digitspernode))
                result=int(result)
            except RecursionError as ERROR:
                result=ERROR
            
        answer = result

    elif "*" in expression:
        a, b = expression.split("*")
        if(not a or not b):
            result="ERROR: improper operation "
        elif(not a.isdigit() or not b.isdigit()):
            result="ERROR: improper operation "
        elif(int(a) == 0 or int(b) == 0):
            result = 0
        else:
            # multiply the 2 numbers by going digit by digit on B and multiplying it to a then passes results 
            # # to addAll to add all them together
            result = functools.reduce(lambda x, y: int(x) + int(y), mathMult(a,b,0,list()))
        answer = result
    else:
        answer = "ERROR: improper operation"

    return answer

# goes through the list of equations looks to see it its + or * then solves it accordingly and pushes it to a new list
def recurseList(n, returnlines, lines, digitspernode):
    """
    Precondition: n is an integer that'll iterate, returnlines is a list of strings of equations, 
        lines is a list of strings of expressions, digitspernode is a constant integer
    Postcondition: returns returnlines a list of string of equations
    """
    if (n == len(lines)):
        return returnlines
    else:
        #lines[n]=lines[n].replace(" ", "")
        if "+" in lines[n]:
            a, b = lines[n].split("+")
            if(not a.isdigit() or not b.isdigit()):
                result="ERROR: improper operation "
            elif(int(a)==0):
                result=b
            elif(int(b)==0):
                result=a
            elif(not a or not b):
                result="ERROR: improper operation "
            
            else:
                # formlist breaks the number int segments then those are passed into mathAdd which address the segments and # 
                # then is assembled back into one number
                try:
                    result = str(int(assemble(0, mathAdd(list(), formlists(list(), a, digitspernode), formlists(list(), b, digitspernode), 0, 0, digitspernode))))
                except RecursionError as ERROR:
                    result=ERROR
                
            arr = appendList(returnlines, lines[n] + " = " + result)

        elif "*" in lines[n]:
            a,b= lines[n].split("*")
            if(not a or not b):
                result="ERROR: improper operation "
            elif(not a.isdigit() or not b.isdigit()):
                result="ERROR: improper operation "
            elif(int(a)==0 or int(b)==0):
                result="0"
            else:
                # multiply the 2 numbers by going digit by digit on B and multiplying it to a then passes results 
                # # to addAll to add all them together
                result = functools.reduce(lambda x, y: int(x) + int(y), mathMult(a,b,0,list()))
            arr = appendList(returnlines, lines[n] + " = " + str(result))
        else:
            arr = appendList(returnlines, lines[n] + " ERROR: improper operation ")
        print (returnlines[n])
    return recurseList(n+1, arr, lines, digitspernode)


def lex(files,tokens):
    print("here")
    tok=""
    state=0
    string =""
    expr=""
    n=0
    files=list(files)

    for char in files:
        tok+=char
        if tok!="0" and tok!="1" and tok!="2" and tok!="3" and tok!="4" and tok!="5" and tok!="6" and tok!="7" and  tok!="8" and tok!="9":
            if expr !="":
                # print (expr)
                tokens.append("NUM:"+expr)
                expr=""
        if tok == " ":
            if state==0:
                tok=""
            else:
                tok=" "
        elif tok=="0" or tok=="1" or tok=="2" or tok=="3" or tok=="4" or tok=="5" or tok=="6" or tok=="7" or  tok=="8" or tok=="9":
            expr += tok
            # print("found Number")
            tok=""
        elif tok=="\n" or tok=="<EOF>":
            tokens.append("NL")
            tok=""
        elif tok=="add":
            # print("found add")
            tokens.append("add")
            tok=""
        elif tok=="multiply":
            # print("found multiply")
            tokens.append("multiply")
            tok=""
        elif tok=="\"":
            if state==0:
                state=1
            elif state==1:
                # print("found a string")
                string=""
                state=0
        elif state ==1:
            string+= char
            tok=""
        elif tok=="(":
            # print("found (")
            tokens.append("(")
            tok=""
        elif tok==")":
            # print("found )")
            tokens.append(")")
            tok=""
        elif tok==",":
            tokens.append(",")
            # print("found ,")
            tok=""
    return(tokens)

        

def parse(toks,digitspernode):
    addToken="add(NUM,NUM)"
    multToken="multiply(NUM,NUM)"
    print (toks)
    a=0
    # print("add" in toks or "multiply" in toks)
    while("add" in toks or "multiply" in toks):
        i =0
        while(i<len(toks)):
            if(i+5<len(toks)):
                if(toks[i]=="NL"):
                    del toks[i]

                if toks[i]+toks[i+1]+toks[i+2][:3]+toks[i+3]+toks[i+4][:3]+toks[i+5]==addToken:
                    # a=int()+int()
                    # print("found")
                    a=int(assemble(0,mathAdd(list(),formlists(list(), toks[i+2][4:],digitspernode), formlists(list(), toks[i+4][4:],digitspernode), 0, 0,digitspernode)))

                    # print("result is int + int",a)
                    del toks[i:i+6]
                    toks.insert(i,"NUM:"+str(a))
                    # print(toks)
            
                elif toks[i]+toks[i+1]+toks[i+2][:3]+toks[i+3]+toks[i+4][:3]+toks[i+5]==multToken:
                    # a=int()*int()
                    a = int((addAll(mathMult(toks[i+2][4:],toks[i+4][4:],0,list()))))
                    # print("result is int * int",a)
                    del toks[i:i+6]
                    toks.insert(i,"NUM:"+str(a))
                    # print(toks) 
            i+=1
    print(toks)

    return toks
def formatOutput(answers, original):
    

   
values = valuesFromTTY(sys.argv)
inputTxt = textFileStream(values[0])
writeLines("out.txt",formatOutput(parse(lex( inputTxt,list()),values[1]),inputTxt))


# writeLines("out.txt", recurseList(0, list(), getLines(inputTxt, list()), values[1]))
checkIfCorrect()