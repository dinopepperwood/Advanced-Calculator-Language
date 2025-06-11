#Math
import math
i = 0
data = []
command = input()
value = ""
j = 0
total = 0
vector1 = [0,0]
vector2 = [0,0]
command = command.replace(" ","")
while i < len(command):
    if command[i].isdigit() or command[i] == ".":
        value += command[i]
    elif command[i] == "[":
        data.append(value)
        value = ""
    elif command[i] == "]" and command[i-len(value)-1] == "[":
        data.append(command[i-len(value)-1])
        if value != "":
            data.append(value)
        data.append(command[i])
        value = ""
    elif (command[i] == "C" or command[i] == "o" or command[i] == "r") and (command[i-1].isdigit() or command[i-1] == "&"):
        if value != "":
            data.append(value)
        data.append(command[i])
        value = ""
    elif (command[i] == "C" or command[i] == "o" or command[i] == "r") and (command[i-1].isdigit() == False or command[i-1] != "&"):
        data.append(command[i])
    elif command[i] == "<" and i + 1 < len(command) and command[i + 1] == "=":
        if value != "":
            data.append(value)
        data.append("<=")
        value = ""
    elif command[i] == "&":
        new = "-"+value
        value = new
    elif command[i] == "V" and command[i+1] == "D" and command[i+2] == "P":
        data.append("VDP")
        i+=2
    elif command[i] == "V" and command[i+1] == "M" and command[i+2] == "1":
        data.append("VM1")
        i+=2
    elif command[i] == "V" and command[i+1] == "M" and command[i+2] == "2":
        data.append("VM2")
        i+=2
    elif command[i] == "V" and command[i+1] == "T" and command[i+2]  == "1":
        data.append("VT1")
        i+=2
    elif command[i] == "V" and command[i+1] == "T" and command[i+2]  == "2":
        data.append("VT2")
        i+=2
    elif command[i] == "V" and command[i+1] == "C" and command[i+2] == "P" and command[i+3] == "3":
        data.append("VCP3")
        i+=3
    elif command[i] == "V" and command[i+1] == "C" and command[i+2] == "P" and command[i+3] == "2":
        data.append("VCP2")
        i+=3
    elif command[i] == "V" and command[i+1] == "C" and command[i+2] == "1":
        data.append("VC1")
        i+=2
    elif command[i] == "V" and command[i+1] == "C" and command[i+2] == "2":
        data.append("VC2")
        i+=2
    elif command[i] == "V" and command[i+1] == "1":
        data.append("V1")
        i+=1
    elif command[i] == "V" and command[i+1] == "2":
        data.append("V2")
        i+=1
    elif command[i] == "V" and command[i+1] == "A":
        data.append("VA")
        i+=1
    elif command[i] == "L":
        data.append("L")
    elif command[i] == "P":
        data.append("P")
    elif command[i] == "S":
        data.append("S")
    elif command[i] == ";":
        data.append(";")
    elif command[i] == ",":
        if value != "":
            data.append(value)
        value = ""
    elif command[i] == "|" and command[(i-len(value))-1] == "|":
        val = float(value)
        data.append(abs(val))
    elif command[i] == "!" and i + 1 < len(command) and command[i + 1] == "=":
        if value != "":
            data.append(value)
        data.append("!=")
        value = ""
    elif command[i] == "*" or command[i] == "+" or command[i] == "-" or command[i] == "/" or command[i] == "^" or (command[i] == "=" and command[i-1] != ">" and command[i-1] != "<" and command[i-1] != "!") or (command[i] == ">" and i >= len(command) and command[i+1] != "=") or (command[i] == "<" and command[i] != "=") or command[i] == "%":
        if value != "":
            data.append(value)
        data.append(command[i])
        value = ""
    elif command[i] == ">" and command[i+1] == "=":
        if value != "":
            data.append(value)
        data.append(">=")
        value = ""
    elif command[i] == "!" and (i + 1 == len(command) or command[i + 1] != "="):
        if value != "":
            data.append(value)
        data.append("!")
        value = ""
    i += 1
if value:
    data.append(float(value))
while j < len(data):
    if data[j] == "+":
        if len(data) > 3 and data[j+2] == "[":
            num = float(data[j+3]) ** (1/float(data[j+1]))
            result = float(data[j-1]) + num
            data.pop(j+4)
            data.pop(j+3)
            data.pop(j+2)
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        elif len(data) > 2 and data[j+1] == "L":
            num = math.log(float(data[j+3]),float(data[j+2]))
            result = float(data[j-1]) + num
            data.pop(j+3)
            data.pop(j+2)
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        else:
            result = float(data[j-1]) + float(data[j+1])
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        data.insert(0,result)
        j = 0
    elif data[j] == "-":
        if len(data) > 3 and data[j+2] == "[":
            num = float(data[j+3]) ** (1/float(data[j+1]))
            result = float(data[j-1]) - num
            data.pop(j+4)
            data.pop(j+3)
            data.pop(j+2)
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        elif len(data) > 2 and data[j+1] == "L":
            num = math.log(float(data[j+3]),float(data[j+2]))
            result = float(data[j-1]) - num
            data.pop(j+3)
            data.pop(j+2)
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        else:
            result = float(data[j-1]) - float(data[j+1])
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        data.insert(0,result)
        j = 0
    elif data[j] == "*":
        if len(data) > 3 and data[j+2] == "[":
            num = float(data[j+3]) ** (1/float(data[j+1]))
            result = float(data[j-1]) * num
            data.pop(j+4)
            data.pop(j+3)
            data.pop(j+2)
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        elif len(data) > 2 and data[j+1] == "L":
            num = math.log(float(data[j+3]),float(data[j+2]))
            result = float(data[j-1]) * num
            data.pop(j+3)
            data.pop(j+2)
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        else:
            result = float(data[j-1]) * float(data[j+1])
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        data.insert(0,result)
        j = 0
    elif data[j] == "/":
        if len(data) > 3 and data[j+2] == "[":
            num = float(data[j+3]) ** (1/float(data[j+1]))
            result = float(data[j-1]) / num
            data.pop(j+4)
            data.pop(j+3)
            data.pop(j+2)
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        elif len(data) > 2 and data[j+1] == "L":
            num = math.log(float(data[j+3]),float(data[j+2]))
            result = float(data[j-1]) / num
            data.pop(j+3)
            data.pop(j+2)
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        else:
            result = float(data[j-1]) / float(data[j+1])
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        data.insert(0,result)
        j = 0
    elif data[j] == "^":
        if len(data) > 3 and data[j+2] == "[":
            num = float(data[j+3]) ** (1/float(data[j+1]))
            result = float(data[j-1]) ** num
            data.pop(j+4)
            data.pop(j+3)
            data.pop(j+2)
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        elif len(data) > 2 and data[j+1] == "L":
            num = math.log(float(data[j+3]),float(data[j+2]))
            result = float(data[j-1]) ^ num
            data.pop(j+3)
            data.pop(j+2)
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        else:
            result = float(data[j-1]) ** float(data[j+1])
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        data.insert(0,result)
        j = 0
    elif data[j] == "%":
        if len(data) > 3 and data[j+2] == "[":
            num = float(data[j+3]) ** (1/float(data[j+1]))
            result = float(data[j-1]) % num
            data.pop(j+4)
            data.pop(j+3)
            data.pop(j+2)
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        elif len(data) > 2 and data[j+1] == "L":
            num = math.log(float(data[j+3]),float(data[j+2]))
            result = float(data[j-1]) % num
            data.pop(j+3)
            data.pop(j+2)
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        else:
            result = float(data[j-1]) % float(data[j+1])
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
        data.insert(0,result)
        j = 0
    elif data[j] == "]" and data[j-2] == "[":
        result = float(data[j-1]) ** (1/float(data[j-3]))
        data.pop(j)
        data.pop(j-1)
        data.pop(j-2)
        data.pop(j-3)
        data.insert(0,result)
        j = 0
    elif data[j] == "P":
        total = 1
        for k in range(int(data[j+1]),int(data[j+2])+1):
            if data[j+3] == "+":
                total*=k+float(data[j+4])
            elif data[j+3] == "-":
                total*=k-float(data[j+4])
            elif data[j+3] == "*":
                total*=k*float(data[j+4])
            elif data[j+3] == "/":
                total*=k/float(data[j+4])
            elif data[j+3] == "^":
                total*=k**float(data[j+4])
            elif data[j+3] == "!":
                total*=math.factorial(k)
        if data[j+3] != "!":
            data.pop(j+4)
        data.pop(j+3)
        data.pop(j+2)
        data.pop(j+1)
        data.pop(j)
        data.insert(0,total)
    elif data[j] == "S":
        total = 0
        for k in range(int(data[j+1]),int(data[j+2])+1):
            if data[j+3] == "+":
                total += k+float(data[j+4])
            elif data[j+3] == "-":
                total += k-float(data[j+4])
            elif data[j+3] == "*":
                total += k*float(data[j+4])
            elif data[j+3] == "/":
                total += k/float(data[j+4])
            elif data[j+3] == "^":
                total += k**float(data[j+4])
            elif data[j+3] == "!":
                total += math.factorial(k)
        if data[j+3] != "!": 
            data.pop(j+4)
        data.pop(j+3)
        data.pop(j+2)
        data.pop(j+1)
        data.pop(j)
        data.insert(0,total)
        j = 0
    elif data[j] == "L":
        result = math.log(float(data[j+2]),float(data[j+1]))
        data.pop(j+2)
        data.pop(j+1)
        data.pop(j)
        data.insert(0,result)
        j = 0
    elif data[j] == "VDP":
        result = (vector1[0] * vector2[0]) + (vector1[1] * vector2[1])
        print(result)
        data.pop(j)
        j = 0
    elif data[j] == "VT1":
        vector3 = []
        vector3.append(vector1[0])
        k = 0
        for k in range(len(vector1)):
            if k != 0 or k != len(vector1):
                if k+4 >= len(vector1):
                    vector3.append(vector1[k-1])
                elif k+4 < len(vector1):
                    vector3.append(vector1[k+3])
        vector3.append(vector1[len(vector1)-1])
        vector3.pop(len(vector3)-2)
        vector3.pop(len(vector3)-2)
        print(vector3)
        data.pop(j)
        j = 0
    elif data[j] == "VT2":
        vector3 = []
        vector3.append(vector2[0])
        k = 0
        for k in range(len(vector2)):
            if k != 0 or k != len(vector2):
                if k+4 >= len(vector2):
                    vector3.append(vector2[k-1])
                elif k+4 < len(vector2):
                    vector3.append(vector2[k+3])
        vector3.append(vector2[len(vector2)-1])
        vector3.pop(len(vector3)-2)
        vector3.pop(len(vector3)-2)
        print(vector3)
        data.pop(j)
        j = 0
    elif data[j] == "VM1":
        total = 0
        for i in range(len(vector1)):
            total += vector1[i]**2
        print(math.sqrt(total))
        total = 0
        data.pop(j)
        j = 0
    elif data[j] == "VM2":
        total = 0
        for i in range(len(vector2)):
            total += vector2[i]**2
        print(math.sqrt(total))
        total = 0
        data.pop(j)
        j = 0
    elif data[j] == "VCP3":
        num1 = (vector1[1]*vector2[2])-(vector2[1]*vector1[2])
        num2 = (vector1[2]*vector2[0])-(vector2[2]*vector1[0])
        num3 = (vector1[0]*vector2[1])-(vector2[0]*vector1[1])
        vector3 = [num1,num2,num3]
        print(vector3)
        data.pop(j)
        j = 0
    elif data[j] == "VCP2":
        result = (vector1[0]*vector2[1]) - (vector1[1]*vector2[0])
        data.pop(j)
        data.insert(0,result)
        j = 0
    elif data[j] == "VC1":
        print(vector1)
        data.pop(j)
    elif data[j] == "VC2":
        print(vector2)
        data.pop(j)
    elif data[j] == "V1":
        vector1.clear()
        j += 1
        while j < len(data) and data[j] != ";":
            vector1.append(float(data[j]))
            data.pop(j)
        j = 0
        data.pop(j+1)
        data.pop(j)
        j = 0
    elif data[j] == "V2":
        vector2.clear()
        j += 1
        while j < len(data) and data[j] != ";":
            vector2.append(float(data[j]))
            data.pop(j)
        j = 0
        data.pop(j+1)
        data.pop(j)
        j = 0
    elif data[j] == "VA":
        num1 = vector1[0] + vector2[0]
        num2 = vector1[1] + vector2[1]
        vector3 = [num1,num2]
        print(vector3)
        data.pop(j)
        j = 0
    elif data[j] == "!":
        result = math.factorial(float(data[j-1]))
        data.pop(j)
        data.pop(j-1)
        data.insert(0,result)
        j = 0
    elif data[j] == "C":
        result = float(data[j-1])
        data.pop(j)
        data.pop(j-1) 
        print(chr(result),end="")
        j = 0
    elif data[j] == "r":
        result = float(data[j-1])
        data.pop(j)
        data.pop(j-1) 
        print(round(result))
        j = 0
    elif data[j] == "o":
        result = float(data[j-1])
        data.pop(j)
        data.pop(j-1) 
        print(result)
        j = 0
    elif data[j] == "=":
        if float(data[j-1]) == float(data[j+1]):
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
            data.insert(0,1)
        else:
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
            data.insert(0,0)
    elif data[j] == "!=":
        if float(data[j-1]) != float(data[j+1]):
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
            data.insert(0,1)
        else:
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
            data.insert(0,0)
    elif data[j] == ">=":
        if float(data[j-1]) >= float(data[j+1]):
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
            data.insert(0,1)
        else:
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
            data.insert(0,0)
    elif data[j] == "<=":
        if float(data[j-1]) <= float(data[j+1]):
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
            data.insert(0,1)
        else:
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
            data.insert(0,0)
    elif data[j] == "<":
        if float(data[j-1]) < float(data[j+1]):
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
            data.insert(0,1)
        else:
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
            data.insert(0,0)
    elif data[j] == ">":
        if float(data[j-1]) > float(data[j+1]):
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
            data.insert(0,1)
        else:
            data.pop(j+1)
            data.pop(j)
            data.pop(j-1)
            data.insert(0,0)
    else:
        j+=1