#!/bin/bash

#text corpus
input=$1

#for naming of output files
prefix=$2

#desired vocab size incl. special tokens
vocab_size=$3

usr_file=user_defined_symbols_simple.txt
if [ $# -ge 4 ]; then
    usr_file=$4
fi
    

spm_train --input=$input --model_prefix $prefix --vocab_size=$vocab_size --character_coverage=1.0 --model_type=unigram --treat_whitespace_as_suffix --unk_id=1 --unk_surface='<unk>' --bos_id=-1 --eos_id=-1 --user_defined_symbols_file=$usr_file   &> ${prefix}.log

awk '{print $1}'  ${prefix}.vocab | sort > ${prefix}.sorted

echo "Done; for diff, use ${prefix}.sorted "
