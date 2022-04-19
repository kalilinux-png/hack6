import ctypes
class DynamicArray:
    def __init__(self):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)
    def append(self,k):
        if self._n==self._capacity:
            print('self._n==self._capacity')
            self._resize()
        self._A[self._n]=k
        self._n+=1
        return self._A
    def __len__(self):
        return self._n
    def __getitem__(self,get):
        if not -(len(self._A))<=get< self._n:
            raise IndexError(f'index not in range(0,{self._n})')
        return self._A[get]
    def _make_array(self,c):
        return (c*ctypes.py_object)()
    def _resize(self):
        B=self._make_array(self._capacity*2)
        for a in range(0,len(self._A)):
            B[a]=self._A[a]
            self._A=B
            B=self._A
        return B
