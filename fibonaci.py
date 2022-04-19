class Fibonaci:
    def __init__(self,first=0,second=1,upto=5):
        self.first=first
        self.second=second
        self.upto=upto
    def increse(self):
        print(self.first)
        c= self.first+self.second
        self.first,self.second=self.second,c
        
    def __iter__(self):
        return self
    def __next__(self):
        print(self.first)
        self.c= self.first+self.second
        self.first,self.second=self.second,self.c
        return self.c
    def draw(self,upto=5):
        return " ".join(str(next(self)) for a in range(upto))
