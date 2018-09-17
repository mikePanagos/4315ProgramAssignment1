#this file is for accessing the text file and making a new one

#removed because requirements say no global variables; can be retrieved by calling getLines(f, []) to return the lines
#lines = list()

#inputTxt = open("input.txt", "r")

#getLines recursively retrieves lines
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

#requires name of text and list
def writeLines(name, lst):
    outf = open(name, "w")
    outf.write("\n".join(lst))


