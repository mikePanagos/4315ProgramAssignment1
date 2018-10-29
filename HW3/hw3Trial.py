import sys 
import re

tokens=[]

# number = re.compile('[0-9]+')
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
    inputTxt = open(inputfile, "r").read()
    inputTxt +="<EOF>"
except Exception as err:
    print(err)
    exit()



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
                    a=int(toks[i+2][4:])+int(toks[i+4][4:])
                    # print("result is int + int",a)
                    del toks[i:i+6]
                    toks.insert(i,"NUM:"+str(a))
                    # print(toks)
            if(i+5<len(toks)):
                if toks[i]+toks[i+1]+toks[i+2][:3]+toks[i+3]+toks[i+4][:3]+toks[i+5]==multToken:
                    a=int(toks[i+2][4:])*int(toks[i+4][4:])
                    # print("result is int * int",a)
                    del toks[i:i+6]
                    toks.insert(i,"NUM:"+str(a))
                    # print(toks) 
            i+=1

    print(toks)
    
   

    
# print(inputTxt)

toks=lex(inputTxt)
parse(toks)