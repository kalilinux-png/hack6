from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for k in attrs:
            print('->',end=' ')
            print(*k,sep=' > ')
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for k in attrs:
            print('->',end=' ')
            print(*k,sep=' > ')

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
test_case=int(input())
string=''
while test_case:
    string+=input()
    test_case-=1

parser.feed(string)

# Learnings : I am not sure what i have  learned  from this but i will remember this for future use and again a lot's of love and thnaks to bhagwan shri krishna (love you so much god really there is no one like you )