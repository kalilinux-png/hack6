class Range:
    def __init__(self,start,stop=None,step=1):
        if step==0:
            raise ValueError('step cannot be zero')
        if stop==None:
           start,stop=0,start
        
        self.lenght=max(0,(stop-start+step-1)//step)
        
        self.start=start
        self.stop=stop
        self.step=step
        
        
        
        
    def __len__(self):
        return self.lenght
    def __getitem__(self,k):
        if k<0:
            k+=len(self)
        if not 0 <=k < self.lenght:
            raise IndexError('index out of range')
        return self.start + k* self.step
    
