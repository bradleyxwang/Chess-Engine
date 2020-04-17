class temp:

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    
    def copy(self, xpos, ypos):
        return temp(xpos, ypos)


temp1 = temp(1, 2)
temp2 = temp(3, 4)

list1 = [temp1, temp2]
list2 = []


for l in list1:
    list2.append(l.copy(l.xpos, l.ypos))

list2[1].ypos = 99

for l in list1:
    print(str(l.xpos) + "," + str(l.ypos))

for l in list2:
    print(str(l.xpos) + "," + str(l.ypos))