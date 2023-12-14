# Both Parts: 306 bytes
*I,=open('14/14.txt')
c=0
# *I,=open(c:=0)
R=range(100)
D={}
S=lambda:print(sum((len(I)-y)*I[y].count('O')for y in R))
while c<4e9:
 *I,=map(list,I)
 for x in R:
  p=0
  for y in R:p=[p,y]['.'>(C:=I[y][x])];I[y][x]='#.'[y>p];I[p][x]=C;p+=C!='.'
 c<1==S();*I,=zip(*I[::-1]);d=c-D.get(s:=str(I),-4e9)+1;c+=(4e9-c)//d*d+1;D[s]=c
S()