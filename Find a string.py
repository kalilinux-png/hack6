
def count_substring(string, sub):
    count=0
    for k in range(len(string)):
        if string[k:k+len(sub)]==sub:
            count+=1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
