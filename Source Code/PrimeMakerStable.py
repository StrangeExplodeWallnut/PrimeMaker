def CreatePrime(f,b):
    p=[]
    for i in range(max([2,f]),b+1):
        flag=False
        for j in range(2,i):
            if i % j == 0:
                flag=True
                break
        if flag==False:
            p.append(i)
    return p
print('PrimeMakerStable')
a=int(input('From:'))
b=int(input('Before:'))
fn=input('FileName:')
dat=CreatePrime(a,b)
f=open(fn+'.txt','w')
f.write(str(dat)[1:-1].replace(' ',''))
f.close()
e=input('Done')
