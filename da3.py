f=open('myfile.txt','r')
s=open('newfile.txt','w')
while True:
    try:
        d=f.readline()
        d=d.split(',')
        avg=(int(d[1])+int(d[2])+int(d[3]))/3
        s.write(f"{d[0]}:{avg}")
        s.write('\n')
    except:
        f.close()
        s.close()
        break
s=open('newfile.txt','r')
print(s.read())
s.close()
