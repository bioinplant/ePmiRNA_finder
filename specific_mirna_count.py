import sys
a=open(sys.argv[1],"r")
b=open(sys.argv[2],"w")
c=open(sys.argv[3],"w")
adict={}
bdict={}
species=[]
for line in a:
    line=line.strip().split()
    if line[0]=="miRNA":
        continue
    else:
        d=open("./treated_ref/uniq_miRNA","r")
        for line1 in d:
            line1=line1.strip().split()
            if line[0] in line1[2]:
                uniq=line1[0]
                slist=line1[2].split(";")
                
        if uniq in adict.keys():
            adict[uniq]+=int(line[1])
        else:
            adict[uniq]=int(line[1])
            uslist=[]
            for i in range(0,len(slist)):
                uslist.append(slist[i].split("=")[1])
            uslist=list(set(uslist))
            species+=uslist
            bdict[uniq]=uslist
for key in adict.keys():
    b.write(key+"\t"+str(adict[key])+"\t"+";".join(bdict[key])+"\n")
for j in set(species):
    c.write(j+"\t"+str(species.count(j))+"\n")
b.close()
c.close()
