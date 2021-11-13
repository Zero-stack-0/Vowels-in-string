name="ShubhamJangid"
vowels="AEIOUaeiou"
a=0
e=0
v=0 #for i 
o=0
u=0

for i in name:
        if(i=='a' or i=='A'):
            a+=1
        elif(i=='e' or i=='E'):
            e+=1
        elif(i=='i' or i=='I'):
            v+=1
        elif(i=='o' or i=='O'):
            o+=1
        elif(i=='u' or i=='U'):
            u+=1
print('a:',a,'e:',e,'i:',v,'o:',o,'u:',u)
