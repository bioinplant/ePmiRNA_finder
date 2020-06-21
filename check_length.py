from collections import defaultdict
import sys
import re
file=open("./index/plant_species_mature_mapped.bwt","r")
plantdict=defaultdict(list)
for line in file:
    line2=line.strip().split()
    mature="-".join(line2[0].split("|")[0].split("-")[0:2])
    pre=line2[2].split("|")[0]
    if len(line2)==7 and mature==pre.replace("MI","mi"):
        value="\t".join([line2[0].split("|")[0],str(line2[3]),str(len(line2[4])+int(line2[3]))])
        plantdict[pre].append(value)

align=open(sys.argv[1],"r")
c=open(sys.argv[2],"w")
pattern = re.compile(r'\d+')
seqdict=defaultdict(list)
for line in align:
    lines=line.strip().split()
    alist=plantdict[lines[2].split("|")[0]]
    start=int(lines[3])
    end=start+len(lines[4])
    if len(lines)==8:
        mismatch=pattern.findall(lines[7])
    else:
        mismatch=0
    for i in range(0,len(alist)):
        miR=alist[i].split()
        diff=abs(start-int(miR[1]))+abs(end-int(miR[2]))
        if diff<3:
            if type(mismatch)==int:
                score=mismatch*4+diff*3
                c.write(lines[0]+"\t"+miR[0]+"\t"+lines[2]+"\t"+str(score)+"\n")
                info=miR[0]+"\t"+str(score)
                seqdict[lines[0]].append(info)
                
            else:
                count=0
                for j in range(0,len(mismatch)):
                    mis=int(mismatch[j])+start
                    if mis in range(max(start,int(miR[1])),min(end,int(miR[2]))+1):
                        count+=1
                if count <=1:
                    score=count*4+diff*3
                    c.write(lines[0]+"\t"+miR[0]+"\t"+lines[2]+"\t"+str(score)+"\n")
                    info=miR[0]+"\t"+str(score)
                    seqdict[lines[0]].append(info)
c.close()
final={}
for key in seqdict.keys():
    inform=seqdict[key]
    sc=12
    for i in range(0,len(inform)):
        seq=inform[i].split()
        if int(seq[1])< sc:
            final[key]=seq[0]
            sc=int(seq[1])
test=""
d=open(sys.argv[3],"w")
for key in final.keys():
    test+=str(key)+"\t"+final[key]+"\n"
d.write(test)
d.close()
f=open(sys.argv[3],"r")
g=open(sys.argv[4],"w")
h=open(sys.argv[5],"w")
bdict={}
for line in f:
    line=line.strip().split()
    count=int(line[0].split("x")[1])
    if line[1] in bdict.keys():
        bdict[line[1]]+=count
    else:
        bdict[line[1]]=count
g.write("miRNA"+"\t"+"counts"+"\n")
for key in bdict.keys():
    g.write(key+"\t"+str(bdict[key])+"\n")
g.close()
f.close()
f=open(sys.argv[3],"r")
hdict={}
pattern=re.compile("miR"+r'\d+')
for line in f:
    line=line.strip().split()
    count=int(line[0].split("x")[1])
    family=pattern.search(line[1]).group()
    if family in hdict.keys():
        hdict[family]+=count
    else:
        hdict[family]=count
h.write("miRNA_family"+"\t"+"counts"+"\n")
for key in hdict.keys():
    h.write(key+"\t"+str(hdict[key])+"\n")
h.close()
