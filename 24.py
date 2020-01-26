# 24.py
# @author Ryan Deng
# @date 20/11/2018
# there is still an error if the number entered is too big
# and some modification is needed to make this more user friendly

#hihihi

# the number and operation used in a list 
operation = ["+", "-", "*", "/"]
num = ["a", "b", "c", "d"]

allOrder = []
allOperation = []
allData = []
answer = ""
allAnswer = []
bufferLs = []

# this function gets all the combinations of the four operations
# and stores it in variable allOperation 
def getOperation():
    for m in operation:
        for n in operation:
            for k in operation:
                operate = [m,n,k,""]
                allOperation.append(operate)

# this function gets all of the combinations of (a,b,c,d)
# and stores it in variable allOrder
def getOrder():
        for q in num:
            for w in num:
                for e in num:
                    for r in num:
                        order = [q,w,e,r]
                        if (len(set(order))==4)and(order not in allOrder):
                            allOrder.append(order)

# this function adds bracket around the combination of data generated
# three types of brackets are added
# 1- 1 bracket that contains 2 numbers
# 2- 1 bracket that contains 3 numbers
# 3- 2 bracket that each contains 2 numbers 
def addBrackets():
    # 1- 1 bracket that contains 2 numbers
    for i in range(3):
        for m in allData:
            temp = []
            data = ""
            for a in m:
                temp.append(a)
            temp.insert(i*2,"(")
            temp.insert(i*2+4,")")
            for b in temp:
                data += b
            bufferLs.append(data)
    # 2- 1 bracket that contains 3 numbers
    for i in range(2):
        for m in allData:
            temp = []
            data = ""
            for a in m:
                temp.append(a)
            temp.insert(i*2,"(")
            temp.insert(i*2+6,")")
            for b in temp:
                data += b
            bufferLs.append(data)
    # 3- 2 bracket that each contains 2 numbers 
    for m in allData:
        temp = []
        data = ""
        for a in m:
            temp.append(a)
        temp.insert(0,"(")
        temp.insert(4,")")
        temp.insert(6,"(")
        temp.insert(10,")")
        for b in temp:
            data += b
        bufferLs.append(data)
        
# this function pairs up each combination of (a,b,c,d)
# with every combination of operations 
def getAllData():
    getOperation()
    getOrder()
    for m in allOrder:
        for n in allOperation:
            data = ""
            for i in range(4):
                data += m[i]
                data += n[i]
            allData.append(data)
    addBrackets()
    for i in bufferLs:
        allData.append(i)

# this is the main function of the program
def main():
    # gets user input
    a = int(input("first number: "))
    b = int(input("second number: "))
    c = int(input("third number: "))
    d = int(input("fourth number: "))

    getAllData()
    for i in allData:
        # try structure is used to prevent ZeroDivisionError
        try:
            result = eval(i)
        except ZeroDivisionError:
            pass
        if result == 24:
            i = i.replace("a",str(a))
            i = i.replace("b",str(b))
            i = i.replace("c",str(c))
            i = i.replace("d",str(d))
            allAnswer.append(i)
    # displaying the answer
    print("There are {} solution(s) in total".format(len(allAnswer)))
    if len(allAnswer)!=0:
        while(True):
            counter = int(input("How many solution(s) do you want me to display: "))
            if counter > 0 and counter <= len(allAnswer):
                break
            print("Please enter a number that is valid!")
            
        for i in range(counter):
            print("{}: {}".format(i+1,allAnswer[i]))
    else:
        print("There is no solution for this pair of numbers")
    return 0


main()
   
            
    
