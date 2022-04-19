import xml.etree.ElementTree as etree

maxdepth = 0

maxdepth = -1
def depth(elem, level):
    global maxdepth
    if elem:
        maxdepth+=1
    for k in elem:
        depth(k,level+1)

    
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)