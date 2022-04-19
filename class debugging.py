class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=OddStream()):
    EvenStream.current=0
    OddStream.current=0
    for _ in range(n):
        print(EvenStream.current)
        print(stream.get_next())
    print(EvenStream.current,'after the for loop')


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "odd":
        print_from_stream(n,OddStream())
    else:
        print_from_stream(n, EvenStream())
