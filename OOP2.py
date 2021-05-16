import math
class circle:
    def __init(self):
        self.__radius=0
    
    def getRad(self):
        return self.__radius
    
    def setRad(self,radPar):
        self.__radius=radPar
    
    def cirPerime(self):
        per = 2 * math.pi * self.__radius  
        return per
    
    def cirArea(self):
        area = math.pi * self.__radius **2
        return area
    
    def __del__(self):
        print("Distructor executed")



rad = int(input("Enter the radius :"))
cir = circle()
cir.setRad(rad)
print("Radius is : {0:5d}".format(cir.getRad()))
print("Perimeter is : {0:8.2f}".format(cir.cirPerime()))
print("Area is : {0:8.2f}".format(cir.cirArea()))
