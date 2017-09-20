# coding = utf-8

s = [1, 2, 3, 4]
print(range(len(s)))

def perm(l):
    if(len(l)<=1):
        return [l]
    r=[]
    for i in range(len(l)):
        s=l[:i]+l[i+1:]
        p=perm(s)
        for x in p:
            r.append(l[i:i+1]+x)
    return r

p = perm(s)
print(p)