import re
try:
    inputTxt = open("out.txt", "r")
except Exception as err:
    print(err)
    exit()

def checkIfCorrect():
    for i, line in enumerate(inputTxt):
        try:
            #values = line.replace("+", " ").replace("*", " ").replace("=", " ").split(" ")
            a, b, c = ["", "", ""]
            op = ""
            if '+' in line:
                op = '+'
                a, b = line.split("+")
                if '=' in b:
                    b, c = b.split("=")
            elif '*' in line:
                op = '*'
                a, b = line.split("*")
                if '=' in b:
                    b, c = b.split("=")
            else:
                raise Exception("Two operands and 1 result required, got: " + str(line.strip("\n")))
            #print("%i %s %s +++ %s ==== %s" % (i+1, line, a, b, c))

            if op == '+':
                if (int(a) + int(b)) == int(c):
                    print("Line %i: Correct" % (i+1))
                else:
                    print("Line %i: INCORRECT - Answer should be %i, got %i" % (i+1, (int(a) + int(b)), int(c)))
            elif op == '*':
                if (int(a) * int(b)) == int(c):
                    print("Line %i: Correct" % (i+1))
                else:
                    print("Line %i: INCORRECT - Answer should be %i, got %i" % (i+1, (int(a) * int(b)), int(c)))
        except Exception as err:
            print("In line %i: %s" % (i+1, err))
