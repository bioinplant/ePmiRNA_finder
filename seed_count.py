import sys
a=open(sys.argv[1],"r")
adict={}
for line in a:
    line=line.strip().split()
    if line[0]=="miRNA":
        continue
    else:
        b=open("./treated_ref/uniq_miRNA","r")
        for line1 in b:
            line1=line1.strip().split()
            if line[0] in line1[2]:
                uniq=line1[0]
        c=open("./treated_ref/mirbase_seed.txt","r")
        for line2 in c:
            line2=line2.strip().split()
            if uniq in line2[3]:
                sname=line2[0]
        if sname in adict.keys():
            adict[sname]+=int(line[1])
        else:
            adict[sname]=int(line[1])
d=open(sys.argv[2],"w")
for key in adict.keys():
    d.write(key+"\t"+str(adict[key])+"\n")
d.close()