def fun(s):
    import re
    return re.fullmatch(r'[\w\d_-]+@[a-zA-Z0-9]+\.[\w]{1,3}$',s) 

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
''' Remember work as hard and smart you can and leave else
on lord krishna '''
''' ever thing that happens and happened was for good and will
be for good '''
