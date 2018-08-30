#this file is for accessing the text file and making a new one

lines = list()

#inputTxt = open("input.txt", "r")

#getLines recursively retrieves lines
def getLines(f):
    line = f.readline()
    if line == "":
        f.close()
    else:
        if line[-1] == '\n':
            line = line[:-1]
        lines.append(line)
        getLines(f)

