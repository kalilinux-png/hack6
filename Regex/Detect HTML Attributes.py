import re
chances=int(input())
for a in range(chances):
    html_code=input()
    pattern=re.compile(r'<\w><\w\s+>')
    ans=pattern.findall(html_code)
    print(ans)
    
''' currently the problem is with regex '''
''' god i ask for help please help me '''
