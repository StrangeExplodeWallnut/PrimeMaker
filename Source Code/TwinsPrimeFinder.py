def FindTP(plist):
    tp=[]
    for i in range(len(plist)-1):
        if int(plist[i+1])-int(plist[i])<=2:
            tp.append([int(plist[i]),int(plist[i+1])])
    return tp
fn=input('FileName:')
outfn=input('OutputFile:')
f=open(fn,'r')
a=f.read()
f.close()
tp=FindTP(a.split(','))
tps=''
for i in tp:
    tps+=str(i[0])+','+str(i[1])
    tps+='\n'
o=open(outfn,'w')
o.write(tps)
o.close()
print(tps)
exits=input()
