class Sequation:
    def __init__(self,data):
        self.data=data
        self._k=-1
    def __next__(self):
        self._k+=1
        if self._k<len(self):
            return(self._data[self._k])
        else:
            raise StopIteration()
        def __iter__(self):
            return self
        def __len__(self):
            return len(self)
        def __getitem__(self,value):
            return self.data[value]
