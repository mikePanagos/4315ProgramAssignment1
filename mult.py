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
# print(assemble(0))
