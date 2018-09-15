# list1 = list()
# list2 = list()
# final = list()


# print("shoud = 311101111")

# # this is a test
# def setlists():
#     del list1[:]
#     del list2[:]
#     del final[:]


# # takes 2 lists goes through them and adds them together in segments if the string is bigger then the
# # segment it will return it as a carry to add onto the next
# def mathAdd(list1, list2, carry, index):
#     # print("carry is ",carry)
#     adding = int(list1[index])+int(list2[index])+int(carry)

#     add = str(adding)
#     if(add == "0"):
#         add = "0000"

#     # check if the 2 segments added together is bigger then the 4 digit segment allowed if so add the last digit to carry
#     if(len(add) > 4):
#         carry = int(add[:1])
#         # print( "carry is =",carry)
#         final.append(add[1:])
#         if (index == len(list1)-1):
#             if(carry):
#                 final.append(carry)
#             return 0
#         mathAdd(list1, list2, carry, index+1)
#     else:
#         final.append(add)

#         carry = 0

#         # print("carry is", carry)
#         if (index == len(list1)-1):
#             return 0
#         mathAdd(list1, list2, carry, index+1)


# # takes the 4 digit segments and combinds them again
# def assemble(index):
#     # print ("index is ",index)
#     # print(" val is ",final[index])
#     if (index == len(final)-1):
#         # print("about to quit")
#         return final[index]
#     return assemble(index+1)+final[index]


# # takes a string and breaks it into 4 digit segments in reversed order
# def formlists(list, num):
#     if(len(num) < 4):
#         list.append(num)
#         return" "
#     list.append(num[-4:])
#     formlists(list, num[:-4])


# # x="199991111"
# # print(x[-4:])            [2]
# # 1000 +9000=  [1][0000][0000]
# formlists(list1, "100001111")
# print(list1)
# formlists(list2, "111110000")
# print(list2)
# mathAdd(list1, list2, 0, 0)
# print("=")
# print(assemble(0))

# setlists()
# print("should be 6")
# formlists(list1, "1000")
# print(list1)
# formlists(list2, "9000")
# print(list2)
# mathAdd(list1, list2, 0, 0)
# print("=")

def addingZeros(index, zeroes):
       
        if(index==0):
            return zeroes
        else:
            zeroes +="0"
            return addingZeros(index-1,zeroes)

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

print("5223333333310000000*500401=")
print(assemble(0, mathMult("52233333333100000001444444444444444444444444444444444444444444444444444444", "500555555559999999999599959996999899949996999399929992994999599695994939929299999999999999999999999999999986986876855401", 0, list())))
# print(addingZeros(5,""))


# def mathMult(list1,list2,index):
