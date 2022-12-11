l1 = [1, 2, 3, 4, 5]


class Junior():
    def get(self):
        print(l1)


class Senior(Junior):
    def setList(self):
        x = 70
        l1.append(x)

    def getList(self):
        super().get()


class Leader(Senior, Junior):
    def remove_ele(self):
        c = 4
        l1.remove(c)

    def addList(self):
        super().setList()

    def newlist(self):
        super().getList()


ch = int(input('what do you want to do '
               '\n1 Leader'
               '\n2.Senior'
               '\n3.Junior'
               '\n4 Enter Your Choice :'))


if ch == 1:
    obj = Leader()

    obj.remove_ele()
    obj.addList()
    obj.newlist()

elif ch == 2:
    obj = Senior()
    obj.setList()
    obj.getList()

elif ch == 3:
    obj = Junior()
    obj.get()

else:
    print('Program Ends!!!')
