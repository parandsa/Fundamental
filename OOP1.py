class rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
    
    def recPerime(self):
        per = (self.width + self.length) * 2
        return per
    
    def recArea(self):
        are = self.width * self.length
        return area
    
    def __str__(self):
        st = "Width is {0:4d}".format(self.width)
        st +=" length is {0:5d}".format(self.length)
        st +="\n"
        st +="perime is {0:3d}".format(self.recPerime())
        st += "area is {0:8d}".format(self.recArea())
        return st


