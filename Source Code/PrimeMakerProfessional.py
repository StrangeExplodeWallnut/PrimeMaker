def CreatePrime(n):
    p=[]
    for i in range(2,n+1):
        flag=False
        for j in p:
            if i % j == 0:
                flag=True
                break
        if flag==False:
            p.append(i)
    return p
print('PrimeMakerProfessional')
a=int(input('Before:'))
fn=input('FileName:')
if fn == '':
    fn = 'Prime In '+str(a)
dat=CreatePrime(a)
f=open(fn+'.txt','w')
f.write(str(dat)[1:-1])
f.close()
print(str(dat)[1:-1])
e=input()
