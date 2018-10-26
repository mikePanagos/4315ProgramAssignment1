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
    inputTxt = open(inputfile, "r").read()
except Exception as err:
    print(err)
    exit()



def lex(files):
    print("here")
    tok=""
    state=0
    string =""
    files=list(files)
    for char in files:
        tok+=char
        if tok == " ":
            if state==0:
                tok=""
            else:
                tok=" "
        elif tok=="\n":
            tok=""
        elif tok=="add":
            print("found add")
            tok=""
        elif tok=="multiply":
            print("found multiply")
            tok=""
        elif tok=="\"":
            if state==0:
                state=1
            elif state==1:
                print("found a string")
                string=""
                state=0
        elif state ==1:
            string+= char
            tok=""
        elif tok=="(":
            print("found (")
            tok=""
        elif tok==")":
            print("found )")
            tok=""
        elif tok==",":
            print("found ,")
            tok=""

        


print(inputTxt)

lex(inputTxt)