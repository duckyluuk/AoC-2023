# Both Parts: 205 bytes
*l,=open(0)
for p in 1,7:
 y=a=b=0
 for h in l:r,d,c=h.split();p>1==exec('d,r=c[2:7],"RDLU"[int(c[-2])]');d=int(d,p+9);f="UDR".find(r)//2;a+="LRD".find(r)//2*d*(2*y+f*d);b+=d;y+=f*d
 print((abs(a)+b+3)//2)