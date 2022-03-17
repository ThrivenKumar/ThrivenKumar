n=raw_input()
n1=n.split()
newarr=[]
newarr2=[]
for i in n1:
    if (i not in newarr) and (i not in newarr2):
        newarr.append(i)
    elif i in newarr:
        newarr.remove(i)
        newarr2.append(i)
print(len(newarr))
