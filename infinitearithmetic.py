from file_maker import *

inputTxt = open("input.txt", "r")
getLines(inputTxt)
# print(lines)


# this file is for the main part evaluate arithmetic operators


# def goThrowList (c):

returnlines = list()


# def strMath(s):

#     if "+" in s:
#         a, b = s.split("+")
#         result = (int(a)+int(b))
#         returnlines.append(s+"="+str(result))
#     elif "*" in s:
#         a, b = s.split("*")
#         result = (int(a)*int(b))
#         returnlines.append(s+"="+str(result))


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
