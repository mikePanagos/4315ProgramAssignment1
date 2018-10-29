# from file_maker import *
import sys
import re

# from checkCorrectness import checkIfCorrect
tokens=[]

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
            if digitspernode <= 0:
                raise ValueError()
        else:
            raise Exception()
    else:
        raise Exception()
except ValueError as err:
    print("Digits Per Node have to be integer greater than 0")
    exit()
except Exception as err:
    print("python3 infinitearithmetic \"input=<filename>;digitsPerNode=<number>\"")
    exit()

try:
    inputTxt = open(inputfile, "r").read()
    inputTxt +="<EOF>"
except Exception as err:
    print(err)
    exit()




# addeds digit segments together 
def mathAdd(list, list1, list2, carry, index):
    if(len(list1) > index and len(list2) > index):
        adding = int(list1[index])+int(list2[index])+int(carry)
    elif(len(list1) > index):
        adding = int(list1[index])+int(carry)
    elif(len(list2) > index):
        adding = int(list2[index])+int(carry)
    else:
        return list

    add = str(adding)
    if(add == "0"):
        add="0"*digitspernode
    if(len(add)<digitspernode and not((index >= len(list1))and(index >= len(list2)) )):
        zeros="0"*(digitspernode-(len(add)))
        add=zeros+add


    # check if the 2 segments added together is bigger then the 4 digit segment allowed if so add the last digit to carry
    if(len(add) > digitspernode):
        carry = int(add[:1])
        list.append(add[1:])
        if (index == len(list1)-1):
            if(carry):
                list.append(str(carry))
            return list
        else:
          return mathAdd(list, list1, list2, carry, index+1)
    else:
        list.append(add)
        carry = 0
        return mathAdd(list, list1, list2, carry, index+1)


# takes the  digit segments and combinds them again
def assemble(index, list):
    if (index == len(list)-1):
        return list[index]
    return assemble(index+1, list)+list[index]


# takes a string and breaks it into 4 digit segments in reversed order
def formlists(list, num):
    if(len(num) < digitspernode):
        if(len(num) > 0):
            list.append(num)
        # print(list)
        return list
    else:
        list.append(num[-digitspernode:])
        return formlists(list, num[:-digitspernode])

# does the multiplication digit by digit 
def mathMult(num1, num2, index, final):
    if(len(num2) > 0):
        # print(num2[-1:])
        zeros="0"*index
        add = str(int(num1)*int(num2[-1:]))+zeros

        if(int(add) == 0):
            return mathMult(num1, num2[:-1], index+1, final)
        else:
            final.append(add)
            return mathMult(num1, num2[:-1], index+1, final)
    else:
        return final

# adds all numbers for multiplication 
def addAll(numberList):
    if(len(numberList)>1):
        add=int(numberList[0])+int(numberList[1])
        numberList.remove(numberList[1])
        numberList[0]=str(add)
        return addAll(numberList)
    else:

        return numberList[0]



# goes through the list of equations looks to see it its + or * then solves it accordingly and pushes it to a new list
def recurseList(n,returnlines, lines):
    if (n == len(lines)):
        return returnlines
    else:
        lines[n]=lines[n].replace(" ", "")
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
                    result =assemble(0,mathAdd(list(),formlists(list(), a), formlists(list(), b), 0, 0))
                    result=int(result)
                    result=str(result)
                except RecursionError as ERROR:
                    result=ERROR
                
            returnlines.append(lines[n]+"="+str(result))

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
                result = (addAll(mathMult(a,b,0,list())))
            returnlines.append(lines[n]+" = "+str(result))
        else:
            returnlines.append(lines[n]+" ERROR: improper operation ")
        print (returnlines[n])
    return recurseList(n+1,returnlines, lines)

def lex(files):
    # print("here")
    tok=""
    state=0
    string =""
    expr=""
    n=0
    files=list(files)

    for char in files:
        tok+=char
        if tok!="0" or tok!="1" or tok!="2" or tok!="3" or tok!="4" or tok!="5" or tok!="6" or tok!="7" or  tok!="8" or tok!="9":
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

        

def parse(toks):
    addToken="add(NUM,NUM)"
    multToken="multiply(NUM,NUM)"
    # print toks
    a=0
    # print("add" in toks or "multiply" in toks)
    while("add" in toks or "multiply" in toks):
        i =0
        while(i<len(toks)):
            # print(toks[i]+toks[i+1]+toks[i+2][:3]+toks[i+3]+toks[i+4][:3]+toks[i+5]+toks[i+6])
            if(i+5<len(toks)):
                if toks[i]+toks[i+1]+toks[i+2][:3]+toks[i+3]+toks[i+4][:3]+toks[i+5]==addToken:
                    # a=int()+int()
                    # print("found")
                    a=assemble(0,mathAdd(list(),formlists(list(), toks[i+2][4:]), formlists(list(), toks[i+4][4:]), 0, 0))
                    # print("result is int + int",a)
                    del toks[i:i+6]
                    toks.insert(i,"NUM:"+str(a))
                    # print(toks)
            if(i+5<len(toks)):
                if toks[i]+toks[i+1]+toks[i+2][:3]+toks[i+3]+toks[i+4][:3]+toks[i+5]==multToken:
                    # a=int()*int()
                    a = (addAll(mathMult(toks[i+2][4:],toks[i+4][4:],0,list())))
                    # print("result is int * int",a)
                    del toks[i:i+6]
                    toks.insert(i,"NUM:"+str(a))
                    # print(toks) 
            i+=1

    print(toks)
    
   

    
# print(inputTxt)

toks=lex(inputTxt)

parse(toks)
# writeLines("out.txt",recurseList(0,list(), getLines(inputTxt, list())))
# checkIfCorrect()