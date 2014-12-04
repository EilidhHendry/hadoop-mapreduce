#!/bin/bash
echo "Assignment 2 - Question 4 - Part 3"
echo "Querying Stack Overflow"
IN="/user/s0925284/exc2/output/task_4_part3_2.out"
OUT="/user/s0925284/exc2/output/task_4_part3_3.out"
MAP="task4mapper_part3_3.py"
RED="task4reducer_part3_3.py"
OUTFILE="Question_4_part3_3"
NUMR=1

hadoop dfs -rmr $OUT

RUN="hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D mapred.text.key.comparator.options=-nr -D mapred.reduce.tasks=$NUMR -input $IN -output $OUT -mapper $MAP -file $MAP -reducer $RED -file $RED"
$RUN
rm -r $OUTFILE
hadoop dfs -copyToLocal $OUT $OUTFILE
echo "Script complete, see output Directory."
