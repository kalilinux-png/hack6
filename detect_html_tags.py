from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for k in attrs:
            print('->',end=' ')
            print(*k,sep=' > ')
    # def handle_endtag(self, tag):
    #     print ("End   :", tag)
    # def handle_startendtag(self, tag, attrs):
    #     print ("Empty :", tag)
    #     for k in attrs:
    #         print('->',end=' ')
    #         print(*k,sep=' > ')

parser = MyHTMLParser()
test_case=int(input())
string=''
while test_case:
    string+=input()
    test_case-=1

parser.feed(string)
    