from collections import defaultdict
softdict=defaultdict(list)
a=open("miranda_result","r")
for line in a:
    line=line.strip()[2:]
    softdict[line].append("miRanda")
b=open("RNAhybrid_result","r")
for line in b:
    line=line.strip()
    softdict[line].append("RNAhybrid")
c=open("pita_17","r")
for line in c:
    line=line.strip().split()
    rela=line[1]+":"+line[0]
    softdict[rela].append("PITA")
d=open("targetscan","r")
for line in d:
    line=line.strip().split()
    rela=line[1]+":"+line[0]
    softdict[rela].append("TargetScan")
e=open("all_prediction.txt","w")
f=open("three_prediction.txt","w")
for key in softdict.keys():
    alist=list(set(softdict[key]))
    e.write(key+"\t"+str(len(alist))+"\t"+";".join(alist)+"\n")
    if len(alist)>2:
        f.write(key+"\t"+str(len(alist))+"\t"+";".join(alist)+"\n")
e.close()
f.close()