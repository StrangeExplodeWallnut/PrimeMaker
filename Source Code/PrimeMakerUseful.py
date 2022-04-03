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
print('PrimeMakerUseful')
a=input('From:')
b=int(input('Before:'))
fn=input('FileName:')
if a == '':
    a = 0
else:
    a=int(a)
if fn == '':
    fn = 'PRIME IN '+str(b)
print('Creating...')
dat=CreatePrime(a,b)
f=open(fn+'.txt','w')
print('Writing...')
f.write(str(dat)[1:-1].replace(' ',''))
print('Closing...')
f.close()
print(str(dat)[1:-1].replace(' ',''))
e=input('Done')
