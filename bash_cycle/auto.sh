#!/bin/bash
# do the caculation automatically

arg1_bgn=0
arg1_end=1
arg1_step=0.5

arg2_bgn=0 
arg2_end=1
arg2_step=0.5

arg3_bgn=0
arg3_end=1
arg3_step=0.5

python_file=printnumber.py

rm -rf ./test
mkdir ./test

for i in `seq ${arg1_bgn} ${arg1_step}  ${arg1_end}`
do 
    for j in  `seq ${arg2_bgn} ${arg2_step}  ${arg2_end}`
    do
        for k in `seq ${arg3_bgn} ${arg3_step}  ${arg3_end}`
        do
        echo $i $j $k
        python3 $python_file $i $j $k > ./test/${i}_${j}_${k}_firsttest.log
        done
    done
done