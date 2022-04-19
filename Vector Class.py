class Vector:
    def __init__(self,d): 
        self.cord=[0]*d # this line does something [0,0,0....d]
    def __setitem__(self,index,value):
        self.cord[index]=value
    def __getitem__(self,index):
        return self.cord[index]
    def __len__(self):
        return len(self.cord)
    def __add__(self,other):
        if len(other)!=len(self): # self is self.cord 3 in 3d 
            raise ValueError('dimensions must be equal')
        result=Vector(len(self)) 
        for a in range(len(self)):
            result[a]=self[a]+other[a]
        return result
    def __str__(self):
        return ' V ' +str(self.cord)[1:-1].replace(',','')+' V '
    
                
