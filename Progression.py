class Progression:
    def __init__(self,start=0):
        self.start=start
    def __next__(self):
        if self.start is None:
            raise StopIteration()
        else:
            self.increase()
            return self.start
    def increase(self):
        self.start+=1
    def __iter__(self):
            return self
class ArthematicPro(Progression):
    def __init__(self,start,step):
        super().__init__(start)
        self.step=step
    def increase(self):
        self.start+=self.step
class GeometricPro(Progression):
    def __init__(self,start=1,r=2):
        super().__init__(start)
        self.r=r
    def increase(self):
        self.start*=self.r
    
