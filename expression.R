options(stringsAsFactors = F)
nameList <- read.table("mirna_file_list",header=F)$V1
matrix <- read.table("miRNA_list",header = F)
for (i in 1:length(nameList)){
  new_table<-read.table(file=as.character(nameList[i]),sep="\t",header = F)[,1:2]
  new_table<-new_table[order(new_table$V2,decreasing = T),]
  #sort &uniq
  new_table<-new_table[!duplicated(new_table$V1),]
  matrix<-merge(matrix,
                new_table,
                by="V1",all.x=TRUE);

  sampleID=unlist(strsplit(as.character(nameList[i]),"_"))[1];
  #sampleID=gsub(".tsv","",sampleID);
  colnames(matrix)[i+1]<- sampleID;
  print(i);
}
matrix[is.na(matrix)]<-0
write.table(matrix,"Count_pla_miRNA.tsv",quote=F, sep='\t',row.names=F)
#transfer to RPM
expfile<- "Count_pla_miRNA.tsv"    
expr_raw<-read.table(expfile,header = F, sep='\t')
lib_read<-read.table("clean_reads.txt",header = F, sep='\t')
find<-match(lib_read$V1,expr_raw[1,])
for (x in 1:length(find)) {
  expr_raw[2:nrow(expr_raw),find[x]]<-as.numeric(expr_raw[2:nrow(expr_raw),find[x]])*(10^6)/lib_read[x,2]
  print(x)
}
write.csv(expr_raw,file="RPM_pla_miRNA.csv")
