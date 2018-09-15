# list1 = list()
# list2 = list(
# final = list()


print("shoud = 311101111")

# this is a test
# def setlists():
    # del list1[:]
    # del list2[:]
    # del final[:]


# takes 2 lists goes through them and adds them together in segments if the string is bigger then the
# segment it will return it as a carry to add onto the next
def mathAdd(list,list1, list2, carry, index):
    # print("carry is ",carry)
    if(len(list1)>index and len(list2)>index):
        adding = int(list1[index])+int(list2[index])+int(carry)
    elif(len(list1)>index):
        adding = int(list1[index])+int(carry)
    elif(len(list2)>index):
        adding = int(list2[index])+int(carry)
    else:
        return list
    

    add = str(adding)
    print (add)
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
          return  mathAdd(list,list1, list2, carry, index+1)
    else:
        list.append(add)

        carry = 0

        # print("carry is", carry)
        return mathAdd(list,list1, list2, carry, index+1)


# takes the 4 digit segments and combinds them again
def assemble(index,list):
    # print(list)
    # print ("index is ",index)
    # print(" val is ",final[index])
    if (index == len(list)-1):
        return list[index]
    return assemble(index+1,list)+list[index]


# takes a string and breaks it into 4 digit segments in reversed order
def formlists(list, num):
    if(len(num)<4):
        list.append(num)
        return list
    if(len(num)> 4):       
        list.append(num[-4:])
        return  formlists(list, num[:-4])


# x="199991111"
# print(x[-4:])            [2]
# 1000 +9000=  [1][0000][0000]
# 
# print(list1)
# 
print("should be 1")
# 
print("=")
print(assemble(0,mathAdd(list(),formlists(list(), "1"), formlists(list(), "111111"), 0, 0)))

# setlists()
print("")
print("")
print("")
print("should be 11")

# print(list1)

# print(list2)

print("=")
print(assemble(0,mathAdd(list(),formlists(list(), "1"), formlists(list(), "10"), 0, 0)))
print("")
print("")
print("")
print("")

# setlists()
print("should be \n21111099999999999999")
# print()
# # print(list1)
# # 
# # print(list2)
# mathAdd(formlists(list(), "12345667890123456789"), formlists(list(), "8765432109876543210"), 0, 0)
# print("=",final)
final =mathAdd(list(),formlists(list(), "1"), formlists(list(), "2962962965966336929297037036296297037036296296703703662962970370369629629637037034000"), 0, 0)
# print(final)
print(assemble(0,final))