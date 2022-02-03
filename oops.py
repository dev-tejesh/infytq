



class check:
    d=1
    def __init__(self,nameee):
        self.__name=nameee
        # print(name)
class another(check):
    def __init__(self, broken):
        self.broken=broken
        self.__name=4
        super().__init__(broken)
        print(self.__name)
c=check("tej")
d=another(333)
# print(d.__name)

