import requests as rq
ans=rq.post('https://in.pinterest.com')
with open('test.html','w') as file:
    file.write(ans.text)

