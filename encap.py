# Section 2 : Encapsulation


class Rectangle:
    mes_rectangles = []

    def __init__(self, long, larg):
        self.__long = long
        self.__larg = larg

    def __repr__(self):
        return f"{self.__long} -  {self.__larg}"

    @property
    def long(self):
        return self.__long
    
    @property
    def larg(self):
        return self.__larg

    @long.setter
    def long(self, value):
        if isinstance(value, (int, float)):
            self.__long = value
        else:
            raise Exception("Valeur incorrect")

    @larg.setter
    def larg(self, value):
        if isinstance(value, (int, float)):
            self.__long = value
        else:
            raise Exception("Valeur incorrect")
        
        # self.__long = value

    #   Les methodes d'instance
    def perimetre(self):
        p = 2 * (self.__long + self.__larg)
        return p

    # def surface(self, multiple):
    #     s = self.long * self.larg
    #     return s * multiple

    #   Les methodes de classe
    @classmethod
    def add(cls, rectangle):
        cls.mes_rectangles.append(rectangle)

    #   Les methodes static
    @staticmethod
    def s():
        print("Static method")


r1 = Rectangle(20, 10)
r1.long = 30
print(r1.long)

# print(r1.long, r1.larg)
# print(r1.perimetre())
