def delmark(string):
    return string.replace('"','')
def FindTP(plist):
    tp=[]
    for i in range(len(plist)-1):
        if plist[i+1]-plist[i]<=2:
            tp.append([plist[i],plist[i+1]])
    return tp
fn=input('FileName:')
outfn=input('OutputFile:')
print('Reading...')
f=open(delmark(fn),'r')
a=f.read()
f.close()
print('Finding...')
p=a.split(',')
if outfn == '':
    outfn = 'TWINS PRIME IN '+max(p)
p=[int(i) for i in p]
p=FindTP(p)
tp=''
for i in p:
    tp+=str(i[0])+','+str(i[1])+';'
tp=tp[:-1]
print('Writing...')
o=open(outfn+'.txt','w')
o.write(tp)
o.close()
print(tp)
e=input('Done')
