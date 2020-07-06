# ePmiRNA_finder
Multi-layer feature selection methods and classifiers for plant-derived miRNA identification from animal miRNA sequencing data.

Here we take human sRNA-seq as an example.

---

## 1.Preparation
Please ensure that the following software or modules were installed.

- Dnapi
- Cutadapt
- Fastx_collapser
- Bowtie
- Python
   - collections
   - sys
   - re
- RNAhybrid
- Miranda
- Pita
- Targetscan
- R

## 2.Identification

```
bash identify_miRNA_fq_strict.bash raw_data.fastq outdir_name outdir_path hsamiRNA_index piRNA_index Rfam_index human_genome_index microbiome_index 
```

- hsamiRNA （http://www.mir-base.org/）
- piRNA (http://www.regulatoryrna.org/database/piRNA/)
- Rfam (https://rfam.xfam.org/)
- human genome (http://asia.ensembl.org/index.html)
- human microbiome (http://www.hmpdacc.org/HMRGD/)


## 3.Classification

- Based on seed-region

```
python seed_count.py miRNA_result.txt output_miRNA.txt
```

- Based on sequence

```
python specific_mirna_count.py miRNA_result.txt output_miRNA.txt output_species.txt
```
## 4.Calculation
```
Rscript expression.R 
```

The following files need to be provided in the run directory.

- All "output\_miRNA.txt" file names were recorded and named as **"mirna\_file_list"**
- All miRNA names were recorded and named as **"miRNA_list"**
- Clean reads of all samples were recorded, the first column was the sample name, the second column was the number pf clean reads, and named as **"clean_reads.txt"**

## 5.Target Prediction

- RNAhybrid

```
RNAhybrid -t human_UTR.fa -q mirna.fa   -b 100 -c -f 2,8 -m 100000 -e -17 -s 3utr_human>test_RNAhybrid
```

- Miranda

```
miranda mirna.fa human_UTR.fa -en -17 -strict -sc 150 > test_miranda
```

- Pita

```
pita_prediction.pl -utr human_UTR.fa -mir mirna.fa -prefix pita -gxp
``` 

- Targetscan

```
perl targetscan_70.pl  ts_mirna.txt ts_human_UTR.fa targetscan
```

- Integrate prediction results

```
bash target.bash
```
