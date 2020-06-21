cut -d ":" -f 1,3 test_RNAhybrid|awk -F ":" '{print $2 ":" $1}'>RNAhybrid_result
grep '>>' test_miranda |cut -f1,2|tr '\t' ':' >miranda_result
awk '{if($13<-17)print $0}' pita_pita_results.tab>pita_17

python overlap.py