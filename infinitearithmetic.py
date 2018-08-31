from file_maker import *

inputTxt = open("input.txt", "r")
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
