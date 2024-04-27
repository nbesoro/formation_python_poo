# Section 0 : Introduction
# Section 1 : Les Fondamentaux de la POO en Python
# Section 2 : Encapsulation et Héritage
# Section 3 : Polymorphisme et Méthodes Spéciales



class Rectangle:
    mes_rectangles = []
    def __init__(self, long, larg):
        self.long = long
        self.larg = larg
    def __repr__(self):
        return f"{self.long} -  {self.larg}"
    
    #   Les methodes d'instance
    def perimetre(self):
        p = 2 * (self.long + self.larg)
        return p
    
    def surface(self, multiple):
        s = self.long * self.larg
        return s * multiple
    
    #   Les methodes de classe
    @classmethod
    def add(cls, rectangle):
        cls.mes_rectangles.append(rectangle)
    #   Les methodes static
    @staticmethod
    def s():
        print("Static method")
    

r1 = Rectangle(20, 10)
r2 = Rectangle(25, 15)
r3 = Rectangle(10, 5)

Rectangle.add(r1)
Rectangle.add(r2)
Rectangle.add(r3)

print(Rectangle.mes_rectangles)


# def perimetre(long, larg):
#     p = 2 * (long + larg)
#     return p



# p = perimetre(20, 10)




# def surface(long, larg):
#     s = long * larg
#     return s


# print(surface(20, 10))