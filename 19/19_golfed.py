# Both Parts: 645 Bytes
B=C=S=0
I={}
T=str.split;E=eval
for l in open(0):
 if' '>l:S=1
 elif S:
  p='in';exec(l[1:~(l[-2]>"|")].replace(*',;'))
  while'Z'<p:q=0;[p:=r[q:=-1]for r in I[p]if-~q&(len(r)<2or E(r[0]))];B+=p<'B'and x+m+a+s
 else:n,r=T(l[:-2],"{");I[n]=*map(T,T(r,','),':'*4),
Q=[('in',*[1,4000]*4)]
for p,x,X,m,M,a,A,s,S in Q:
 C+=~(X-x)*~(M-m)*~(A-a)*~(S-s)*(p<"B")
 if(x<X)*(m<M)*(a<A)*(s<S)*(p in I):
  for r in I[p]:F=len(r)>1;Q+=E("(r[F],x,X,m,M,a,A,s,S)".replace(*'~~'[F*2:]or[L:=(v:=r[0][0]).lower(),U:=v.upper(),f'max({L},{(n:=E(r[0][2:]))+1})',f'min({U},{n-1})'][(o:=r[0][1]=="<")::2])),;exec([f"{U}=min({U},{n})",f"{L}=max({L},{n})"][o])
print(B,C)