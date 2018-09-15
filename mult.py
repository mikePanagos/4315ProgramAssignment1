# takes 2 lists goes through them and adds them together in segments if the string is bigger then the
# segment it will return it as a carry to add onto the next


def mathAdd(list, list1, list2, carry, index):
    # print("carry is ",carry)
    if(len(list1) < 0):
        adding = int(list2[index])+int(carry)
    if(len(list2) < 0):
        adding = int(list1[index])+int(carry)
    else:
        adding = int(list1[index])+int(list2[index])+int(carry)

    add = str(adding)
    # print (add)
    if(add == "0"):
        add = "0000"

    # check if the 2 segments added together is bigger then the 4 digit segment allowed if so add the last digit to carry
    if(len(add) > 4):
        carry = int(add[:1])
        # print( "carry is =",carry)
        list.append(add[1:])
        # print ("the list is",list)
        if (index == len(list1)-1):
            if(carry):
                list.append(str(carry))

            return list
        else:
          return mathAdd(list, list1, list2, carry, index+1)
    else:
        list.append(add)

        carry = 0

        # print("carry is", carry)
        if (index == len(list1)-1):
            return list
        else:
           return mathAdd(list, list1, list2, carry, index+1)

# takes a string and breaks it into 4 digit segments in reversed order
def formlists(list, num):
    if(len(num) < 4):
        if(len(num) > 0):
            list.append(num)
        return list
    else:
        list.append(num[-4:])
        return formlists(list, num[:-4])

def addingZeros(index, zeroes):

    if(index == 0):
        return zeroes
    else:
        zeroes += "0"
        return addingZeros(index-1, zeroes)

    # print(assemble(0))


def mathMult(num1, num2, index, final):

    if(len(num2) > 0):
        # print(num2[-1:])
        zeros = addingZeros(index, "")
        add = str(int(num1)*int(num2[-1:]))+zeros

        if(int(add) == 0):
            return mathMult(num1, num2[:-1], index+1, final)
        else:
            final.append(add)
            return mathMult(num1, num2[:-1], index+1, final)
        # print(num2[:-1])
    else:
        # print(final)
        return final


def assemble(index, list):
    # print(list)
    # print ("index is ",index)
    # print(" val is ",final[index])
    if (index == len(list)-1):
        return int(list[index])
    return assemble(index+1, list)+int(list[index])


# def addAll(list):
#     return list

print("5223333333310000000*500401=")
print( mathMult("52233333333100000001444444444444444444444444444444444444444444444444444444", "500555555559999999999599959996999899949996999399929992994999599695994939929299999999999999999999999999999986986876855401", 0, list()))
# print(addingZeros(5,""))