def CreatePrime(n):
    p=[]
    for i in range(2,n+1):
        flag=False
        for j in p:
            if i % j == 0:
                flag=True
        if flag==False:
            p.append(i)
    return p
print('PrimeMakerPlus')
a=int(input('Before:'))
fn=input('FileName:')
if fn == '':
    fn = 'PRIME'
dat=CreatePrime(a)
f=open(fn+'.txt','w')
f.write(str(dat)[1:-1].replace(' ',''))
f.close()
print(str(dat)[1:-1].replace(' ',''))
e=input('Done')
