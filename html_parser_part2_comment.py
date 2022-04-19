
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        # print ("Comment  :",data)
        # print('data split--->',data.split('\n'))
        if len(data.split('\n')) > 1:
            print('>>> Multi-line Comment')
            print(data)
            # print(type(data))
        else:
            print('>>> Single-line Comment')
            print(data)
        # print(data.split('\n'))
    def handle_data(self, data):
        if data=='\n':
            return 
        print (">>> Data")
        print( data)

test_case=int(input())
string=''
parser=MyHTMLParser()
while test_case:
    string+=input()+'\n'
    test_case-=1
parser.feed(string)