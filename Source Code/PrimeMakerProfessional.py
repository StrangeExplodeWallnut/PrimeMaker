def delmark(string):
    return string.replace('"','')
def CreatePrime(n,before=[2]):
    p=before
    for i in range(p[-1]+1,n+1):
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
add=input('AddFileName:')
if fn == '':
    fn = 'PRIME IN '+str(a)
if add == '':
    o=[2]
else:
    print('Opening AddFile...')
    af=open(delmark(add),'r')
    o=af.read()
    af.close()
    o=o.split(',')
    for i in range(len(o)):
        o[i]=int(o[i])
print('Creating...')
dat=CreatePrime(a,o)
f=open(fn+'.txt','w')
print('Writing...')
f.write(str(dat)[1:-1].replace(' ',''))
print('Closing...')
f.close()
print(str(dat)[1:-1].replace(' ',''))
e=input('Done')
