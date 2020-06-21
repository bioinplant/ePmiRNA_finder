adp=$(python dnapi.py $1)
cd $3
mkdir $2
cutadapt --cores 20 --quality-base=33 -e 0.1 -q 20 -O 3 -m 18 -M 30 -a ${adp} --output $2/$2.fq $1
fastx_collapser="/data/biosoft/fastx_toolkit-0.0.14/src/fastx_collapser/fastx_collapser"
	
# file: 
rawfq=$2/$2.fq
rawfa=$2.fa
	
collapsed=$2_collapsed.fa
#clippered=$2_clippered.fa

fastx_collapser -i ${rawfq} -o ${rawfa}
cat ${rawfa} | awk -F '-' '{if($1~/>/) print $1"_x"$2;else print $0}' | sed 's/>/>seq_/' > ${collapsed}


printf "\n**** File $1 mapping hsamiRNA **** \n"
bowtie $4 -p 20 -f ${collapsed} -v 2 --un $2/$2_collapsed_unaligned_hsamiR.fa > $2/$2_collapsed_aligned_hsamiRNA.bwt

printf "\n**** File $1 mapping piRNA **** \n"
bowtie $5 -p 20 -f $2/$2_collapsed_unaligned_hsamiR.fa -v 2 --un $2/$2_collapsed_unaligned_hsapi.fa > $2/$2_collapsed_aligned_hsapi.bwt

printf "\n**** File $1 mapping Rfam **** \n"
bowtie $6 -p 20 -f $2/$2_collapsed_unaligned_hsapi.fa -v 2 --un $2/$2_collapsed_unaligned_Rfam.fa > $2/$2_collapsed_aligned_Rfam.bwt

printf "\n**** File $1 mapping hg19 genome **** \n"
bowtie $7 -p 20 -f $2/$2_collapsed_unaligned_Rfam.fa -v 1 --un $2/$2_collapsed_unaligned_hg19.fa > $2/$2_collapsed_aligned_hg19.bwt

printf "\n**** File $1 mapping microbiome **** \n"
bowtie $8 -p 20 -f $2/$2_collapsed_unaligned_hg19.fa -v 1 --un $2/$2_collapsed_unaligned_microbiome.fa > $2/$2_collapsed_aligned_microbiome.bwt

printf "\n**** File $1 quantification by bowtie (plant stemloop)**** \n"
bowtie  ./index/plant_miRNA_precursor/miRNA_precursor  -p 20 -f $2/$2_collapsed_unaligned_microbiome.fa -v 3 >$2/$2_align_plant.bwt

mkdir ./res	
python check_length.py $2/$2_align_plant.bwt $2/$2_match.txt $2/$2_map_result.txt ./res/$2_miRNA_result.txt ./res/$2_miRNA_family_result.txt

#rm ${rawfq}
printf "\n**** File $2 done! Results in dir. res/ **** \n\n"
