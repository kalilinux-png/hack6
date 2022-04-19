import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    deep=[elem ]
    if len(elem):
        maxdepth+=1
    while deep:
        for k in deep[0]:
            deep.append(k)
            if len(k):
                print(k,len(k))
                maxdepth+=1
        del deep[0]

    # your code goes here

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)